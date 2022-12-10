from HashToDocx import HashToDocx

doc = HashToDocx(['filename', 'size', 'md5', 'sha1', 'sha256', 'ctime', 'mtime', 'atime'])
doc.scanDir('sample')
doc.save('123.docx')