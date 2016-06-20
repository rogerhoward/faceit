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



select * 
from AgLibraryKeywordFace AS Faces
inner join AgLibraryKeyword AS Keyword on Faces.tag = Keyword.id_local
where Keyword.name = 'Arthur Thomas Parker'
ORDER BY face
LIMIT 5000

select Image, Faces.bl_x, Faces.bl_y, Faces.br_x, Faces.br_y, Faces.tl_x, Faces.tl_y, Faces.tr_x, Faces.tr_y, Faces.imageOrientation, Faces.orientation,  Image.fileWidth, Image.fileHeight
File.baseName || '.jpg' as Filename
from AgLibraryFace AS Faces
inner join AgLibraryKeywordFace AS KwFace on Faces.id_local = KwFace.face
inner join AgLibraryKeyword AS Keyword on KwFace.tag = Keyword.id_local
inner join Adobe_images AS Image ON Faces.image = Image.id_local
inner join AgLibraryFile AS File on Image.rootFile = File.id_local
where Keyword.name = 'Arthur Thomas Parker'
ORDER BY image


select Image, Faces.bl_x, Faces.bl_y, Faces.br_x, Faces.br_y, Faces.tl_x, Faces.tl_y, Faces.tr_x, Faces.tr_y, Faces.imageOrientation,  Image.fileWidth, Image.fileHeight,
File.baseName || '.jpg' as Filename
from AgLibraryFace AS Faces
inner join AgLibraryKeywordFace AS KwFace on Faces.id_local = KwFace.face
inner join AgLibraryKeyword AS Keyword on KwFace.tag = Keyword.id_local
inner join Adobe_images AS Image ON Faces.image = Image.id_local
inner join AgLibraryFile AS File on Image.rootFile = File.id_local
where Keyword.name = 'Arthur Thomas Parker' and Faces.imageOrientation = 'AB'
ORDER BY image