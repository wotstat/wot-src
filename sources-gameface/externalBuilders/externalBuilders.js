const path = require("path");
const os = require("os");
const fs = require("fs-extra");
const process = require("process");
const {
  createCache,
  getModifiedFeatures,
  getFeatures,
} = require("./modificationsIndexing/modificationsIndexing");
const { Worker } = require("worker_threads");
const environment = process.env.NODE_ENV || "development";
const IS_DEV = environment === "development";

const BUILD_MODES = {
  fullBuild: "fullBuild",
  modificationBuild: "modificationBuild",
  start: "start",
};
const AUTO_START_FEATURE = process.env.AUTO_START_FEATURE;
const COUNT_OF_WORKERS = process.env.WEBPACK_WORKERS || 2;
const buildMode = BUILD_MODES[process.env.BUILD_MODE] || BUILD_MODES.start;

const projectDirectory = path.resolve(__dirname, "..");
const buildDirectory = path.join(projectDirectory, IS_DEV ? "_dev" : "_dist");

const BYTES_IN_GB = Math.pow(1024, 3);
const MAX_WORKER_MEMORY_GB = 5.0;

const getOptimalWorkersCount = (desiredCount) => {
  const cpuCores = os.cpus().length;
  const systemFreeMemGB = os.freemem() / BYTES_IN_GB;

  const maxWorkersByRam = Math.floor(systemFreeMemGB / MAX_WORKER_MEMORY_GB);
  const maxWorkersByCpu = cpuCores;

  const optimal = Math.min(desiredCount, maxWorkersByRam, maxWorkersByCpu);

  return Math.max(1, optimal);
};

const clear = (feature) => {
  const buildFeaturePath = path.join(buildDirectory, feature.replace("views", "production"));
  const chunksPath = path.join(
    buildDirectory,
    "production",
    "chunks",
    /([^\\/]*)\/*$/.exec(feature)[1],
  );
  const vendorPaths = path.join(buildDirectory, feature.replace("views", "production/lib"));

  if (fs.existsSync(buildFeaturePath)) {
    fs.rmSync(buildFeaturePath, { recursive: true });
  }
  if (fs.existsSync(chunksPath)) {
    fs.rmSync(chunksPath, { recursive: true });
  }
  if (fs.existsSync(vendorPaths)) {
    fs.rmSync(vendorPaths, { recursive: true });
  }
};

const modificationBuild = () => {
  const modifiedFeatures = getModifiedFeatures();
  if (modifiedFeatures.length > 0) {
    if (modifiedFeatures.includes("shared")) {
      fullBuild();
    } else {
      modifiedFeatures.forEach((feature) => clear(feature));
      buildFeatures(modifiedFeatures);
    }
  } else {
    // eslint-disable-next-line no-console
    console.log("\x1b[32m%s\x1b[0m", `Nothing to built`);
  }
};

const fullBuild = () => {
  fs.emptyDirSync(buildDirectory);
  const features = getFeatures();
  buildFeatures(features);
};

const buildFeatures = (features) => {
  const desiredCount = features.length > COUNT_OF_WORKERS ? COUNT_OF_WORKERS : 1;
  const countOfWorkers = getOptimalWorkersCount(desiredCount);

  const workersFeatures = Array.from({ length: countOfWorkers }, () => []);
  features.forEach((feature, index) => {
    workersFeatures[index % countOfWorkers].push(feature);
  });

  const builders = workersFeatures.map((featList) => createBuilders(featList));
  Promise.all(builders)
    .then(() => {
      if (!IS_DEV) {
        createCache();
      }

      // eslint-disable-next-line no-console
      console.log("\x1b[32m%s\x1b[0m", `All features successfully built`);
    })
    .catch(() => {
      process.exit(-1);
      console.error("\x1b[31m%s\x1b[0m", "Build failed!");
    });
};

const createBuilders = (features) => {
  return new Promise((resolve, reject) => {
    const builder = new Worker("./externalBuilders/workers/BuildWorker.js", {
      workerData: { features },
    });
    builder.on("error", (error) => {
      console.error(error);
      reject();
    });
    builder.on("exit", (code) => {
      if (code !== 0) {
        reject(new Error(`Worker stopped with exit code ${code}`));
      }
      resolve();
    });
  });
};

async function questionToStart(features) {
  const readline = require("readline");
  const util = require("util");
  const lineInterface = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });
  const question = util.promisify(lineInterface.question).bind(lineInterface);

  features.forEach((feature, index) => {
    // eslint-disable-next-line no-console
    console.log(`${index} - ${feature}`);
  });
  const answer = await question("Which feature do you want to work with?\n\nNumber: ");
  lineInterface.close();

  return features[answer];
}

const startWatchBuilder = (feature) => {
  process.title = `webpack -> ${feature}`;
  // eslint-disable-next-line no-console
  console.log(`Run build and watch ${feature}...`);
  clear(feature);
  const builder = new Worker("./externalBuilders/workers/WatchWorker.js", {
    workerData: { feature },
  });
  builder.on("error", (error) => {
    console.error(error);
  });
};

const start = () => {
  const features = getFeatures();
  if (AUTO_START_FEATURE) {
    startWatchBuilder(features.find((feature) => feature.endsWith(AUTO_START_FEATURE)));
  } else {
    questionToStart(features).then((feature) => {
      startWatchBuilder(feature);
    });
  }
};

const run = () => {
  switch (buildMode) {
    case BUILD_MODES.fullBuild:
      return fullBuild();
    case BUILD_MODES.modificationBuild:
      return modificationBuild();
    case BUILD_MODES.start:
    default:
      return start();
  }
};

run();
