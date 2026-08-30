from idlelib.configHandler import idleConf
menudefs = [
 (
  b'file',
  [
   97, 
   98, 
   99, 
   100, 
   101, 
   96, 
   102, 
   103, 
   104, 
   96, 
   105, 
   96, 
   106, 
   107]),
 (
  b'edit',
  [
   108, 
   109, 
   96, 
   110, 
   111, 
   112, 
   113, 
   96, 
   114, 
   115, 
   116, 
   117, 
   118, 
   119]),
 (
  b'format',
  [
   120, 
   121, 
   122, 
   123, 
   124, 
   125, 
   126, 
   127]),
 (
  b'run',
  [
   (b'Python Shell', b'<<open-python-shell>>')]),
 (
  b'shell',
  [
   (b'_View Last Restart', b'<<view-restart>>'),
   (b'_Restart Shell', b'<<restart-shell>>'),
   None,
   (b'_Interrupt Execution', b'<<interrupt-execution>>')]),
 (
  b'debug',
  [
   (b'_Go to File/Line', b'<<goto-file-line>>'),
   (b'!_Debugger', b'<<toggle-debugger>>'),
   (b'_Stack Viewer', b'<<open-stack-viewer>>'),
   (b'!_Auto-open Stack Viewer', b'<<toggle-jit-stack-viewer>>')]),
 (
  b'options',
  [
   (b'Configure _IDLE', b'<<open-config-dialog>>'),
   None]),
 (
  b'help',
  [
   (b'_About IDLE', b'<<about-idle>>'),
   None,
   (b'_IDLE Help', b'<<help>>'),
   (b'Python _Docs', b'<<python-docs>>')])]
default_keydefs = idleConf.GetCurrentKeySet()
