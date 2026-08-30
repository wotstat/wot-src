import logging, time, weakref, threading
from Queue import PriorityQueue, Empty as QueueEmptyError
_logger = logging.getLogger(__name__)
INFINITE_QUEUE_SIZE = 0
_LOW_PRIORITY = 10
_DEFAULT_PRIORITY = 1

class Job(object):

    def doWork(self, worker):
        raise NotImplementedError
        return


class TerminateJob(Job):

    def doWork(self, worker):
        worker.terminate()
        return


class Worker(threading.Thread):

    def __init__(self, jobsQueue, name=None):
        super(Worker, self).__init__(name=name)
        self.__queueRef = weakref.ref(jobsQueue)
        self._terminated = False
        return

    def __del__(self):
        _logger.debug(b'Worker has been deleted: %s', self)
        return

    def terminate(self):
        self._terminated = True
        return

    def run(self):
        while not self._terminated:
            try:
                queue = self.__queueRef()
                if queue is not None:
                    _, job = queue.get()
                    job.doWork(self)
                    queue.task_done()
                else:
                    self.terminate()
                    break
                time.sleep(0.001)
            except Exception:
                _logger.exception(b'Exception raises in Worker: %r', self)

        return

    def __repr__(self):
        if not self._terminated:
            return b'%s(name = %s)' % (
             self.__class__.__name__, self.name)
        return b'%s(terminated)' % self.__class__.__name__


class ThreadPool(object):

    def __init__(self, workersLimit, queueLimit=-1):
        self._jobs = PriorityQueue(queueLimit)
        self._running = False
        self._workers = []
        self._workersLimit = workersLimit
        return

    @property
    def isRunning(self):
        return self._running

    def start(self):
        for _ in xrange(self._workersLimit):
            worker = self._createNewWorker()
            try:
                worker.start()
            except Exception:
                _logger.error(b'Worker has not been started properly: %r', worker)
            else:
                self._workers.append(worker)

        self._running = True
        return

    def stop(self):
        self._running = False
        try:
            while True:
                self._jobs.get_nowait()

        except QueueEmptyError:
            pass

        for _ in self._workers:
            self._jobs.put_nowait((_LOW_PRIORITY, TerminateJob()))

        self._workers = []
        return

    def _createNewWorker(self):
        return Worker(self._jobs)

    def putLowPriorityJob(self, job):
        if not self._running:
            _logger.error(b'Thread pool is not running. Trying to put new job: %r', job)
            return
        self._jobs.put_nowait((_LOW_PRIORITY, job))
        return

    def putJob(self, job):
        if not self._running:
            _logger.error(b'Thread pool is not running. Trying to put new job: %r', job)
            return
        self._jobs.put_nowait((_DEFAULT_PRIORITY, job))
        return

    def __repr__(self):
        return b'%s(workers = %d; jobs = %d)' % (
         self.__class__.__name__, len(self._workers), self._jobs.qsize())
