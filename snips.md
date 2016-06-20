convert -define jpeg:size=512x512 original.jpeg  -thumbnail 100x100^ -gravity center -extent 100x100  thumbnail.jpeg


mogrify -path ~/Desktop/squares -define jpeg:size=512x512 -thumbnail 256x256^ -gravity center -extent 256x256 /Volumes/Projects/faces/arthur/_crops/*




mogrify -path ~/Desktop/squares -define jpeg:extent=2MB dsc_big/*