select Folder.pathFromRoot, File.baseName, File.extension, Hist.*, Faces.*, Keyword.name
from  Adobe_libraryImageFaceProcessHistory AS Hist
inner join Adobe_images AS Img ON Hist.image = Img.id_local
inner join AgLibraryFile AS File on  Img.rootFile = File.id_local
inner join AgLibraryFolder AS Folder on File.folder = Folder.id_local
inner join AgLibraryFace AS Faces on Hist.image = Faces.image
inner join AgLibraryKeywordFace AS KwFace on Faces.id_local = KwFace.face
inner join AgLibraryKeyword AS Keyword on KwFace.tag = Keyword.id_local
where Keyword.name = 'Arthur Thomas Parker'



select *
from AgLibraryFace AS Faces
inner join AgLibraryKeywordFace AS KwFace on Faces.id_local = KwFace.face
inner join AgLibraryKeyword AS Keyword on KwFace.tag = Keyword.id_local
where Keyword.name = 'Arthur Thomas Parker'




select Faces.*, File.*
from AgLibraryFace AS Faces
inner join AgLibraryKeywordFace AS KwFace on Faces.id_local = KwFace.face
inner join AgLibraryKeyword AS Keyword on KwFace.tag = Keyword.id_local

inner join Adobe_images AS Image ON Faces.image = Image.id_local
inner join AgLibraryFile AS File on Image.rootFile = File.id_local

where Keyword.name = 'Arthur Thomas Parker'
ORDER BY image