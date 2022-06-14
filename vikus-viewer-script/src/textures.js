const fs = require("fs");
const path = require("path");
const cascade = require("./cascade.js");
const sharpsheet = require("sharpsheet");

exports.run = async function textures(inputPath, options) {

  const textureRes1 = options.largeSize || 4096;
  const textureRes2 = options.mediumSize || 1024;
  const textureRes3 = options.spriteSize || 256;
  const outputPath = options.output || "./data";
  const textureFormat = options.textureFormat || "jpg";
  const textureQuality = options.textureQuality || 60;
  const skipExisting = options.skip || false;
  const spriteFormat = options.spriteFormat || "jpg";
  const spriteQuality = options.spriteQuality || 70;
  const multipe = options.multipe || false;

  const workPath = createPath(path.resolve(outputPath));
  const spritesPath = createPath(workPath + "/sprites");
  const tmpPath = createPath(workPath + "/tmp");
  const textureRes1Path = createPath(workPath + "/" + textureRes1);
  const textureRes2Path = createPath(workPath + "/" + textureRes2);
  const textureRes3Path = createPath(tmpPath + "/" + textureRes3);


  const resizeSteps = [
    {
      width: textureRes1,
      height: textureRes1,
      format: textureFormat,
      quality: textureQuality,
      path: textureRes1Path,
    },
    {
      width: textureRes2,
      height: textureRes2,
      format: textureFormat,
      quality: textureQuality,
      path: textureRes2Path,
    },
    {
      width: textureRes3,
      height: textureRes3,
      format: "png",
      quality: 100,
      path: textureRes3Path,
    },
  ];

  console.log("\nlooking for images at ", inputPath);

  const resizer = cascade.run(inputPath, resizeSteps, { skipExisting });

  let spritesheetFiles = []
  for await (const operation of resizer) {
    console.log(operation.progress, operation.file);
    if (operation.log[2]) spritesheetFiles.push(operation.log[2])
    else console.error("Error with file", operation.file);
  }

  if (multipe) {
    // this only works if the _ is only used fpr multipage files
    spritesheetFiles = spritesheetFiles.filter(file => file.indexOf("_") == -1)
  }

  const spriter = await sharpsheet(spritesheetFiles, spritesPath, {
    outputFormat: spriteFormat,
    outputQuality: spriteQuality,
    dimension: 2048
  });

  console.log("done");
}

function createPath(path) {
  if (!fs.existsSync(path)) fs.mkdirSync(path);
  return path;
}

//exports.run('../evoint-scripts/data/thumbnails/0010.png', { output: "../vikus-viewer/data/images" })