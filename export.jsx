// This is a Photoshop script to export all egm files from egm-work.psd
// You can run this script in Adobe Photoshop, File > Scripts > Browse...

function hideAllLayers(parent) {
    parent = parent || app.activeDocument;
    for (var i = 0; i < parent.artLayers.length; i++) {
        parent.artLayers[i].visible = false;
    }
    for (var i = 0; i < parent.layerSets.length; i++) {
        parent.layerSets[i].visible = false;
        hideAllLayers(parent.layerSets[i]);
    }
}

function findAllItemsByName(name, parent, foundItems) {
    parent = parent || app.activeDocument;
    foundItems = foundItems || [];
    for (var i = 0; i < parent.artLayers.length; i++) {
        if (parent.artLayers[i].name === name) {
            foundItems.push(parent.artLayers[i]);
        }
    }
    for (var i = 0; i < parent.layerSets.length; i++) {
        if (parent.layerSets[i].name === name) {
            foundItems.push(parent.layerSets[i]);
        }
        findAllItemsByName(name, parent.layerSets[i], foundItems);
    }
    return foundItems;
}

function formatNumber(num) {
    return (num < 10 ? "0" : "") + num;
}

function exportLayersAsPNG() {
    if (!app.documents.length) {
        alert("There is no open document.");
        return;
    }

    var doc = app.activeDocument;

    var exportFolder = Folder.selectDialog("Select a folder to save PNG files");
    if (!exportFolder) {
        alert("Export folder not selected. Exiting script.");
        return;
    }

    alert("Selected path: " + exportFolder.fsName);

    var pngOpts = new ExportOptionsSaveForWeb();
    pngOpts.format = SaveDocumentType.PNG;
    pngOpts.PNG8 = false; // PNG-24
    pngOpts.transparency = true;
    pngOpts.quality = 100;

    hideAllLayers();

    var boxItems = findAllItemsByName("box");
    if (boxItems.length === 0) {
        alert("The 'box' layer group was not found.");
        return;
    }
    for (var i = 0; i < boxItems.length; i++) {
        boxItems[i].visible = true;
    }

    var nameindex = 1;
    var rainbowLayer, rainbowRevealLayer, normalLayer;

    try {
        rainbowLayer = findAllItemsByName("rainbow")[0];
        rainbowRevealLayer = findAllItemsByName("rainbow reveal")[0];
        normalLayer = findAllItemsByName("normal")[0];
    } catch (e) {
        alert("The (rainbow, rainbow reveal, normal) layer group was not found." + e);
        return;
    }

    for (var i = 1; i <= 50; i++) {
        var layerName = formatNumber(i);

        try {
            var layers = findAllItemsByName(layerName);

            if (layers.length > 0) {
                for (var j = 0; j < layers.length; j++) {
                    layers[j].visible = true;
                }

                try {
                    rainbowLayer.visible = true;
                    var rainbowFilename = "egm" + formatNumber(nameindex) + ".twx.png";
                    var rainbowFile = new File(exportFolder + "/" + rainbowFilename);
                    doc.exportDocument(rainbowFile, ExportType.SAVEFORWEB, pngOpts);
                    nameindex++;
                    rainbowLayer.visible = false;

                    rainbowRevealLayer.visible = true;
                    normalLayer.visible = true;
                    var rainbowRevealFilename = "egm" + formatNumber(nameindex) + ".twx.png";
                    var rainbowRevealFile = new File(exportFolder + "/" + rainbowRevealFilename);
                    doc.exportDocument(rainbowRevealFile, ExportType.SAVEFORWEB, pngOpts);
                    nameindex++;
                    rainbowRevealLayer.visible = false;


                    var normalFilename = "egm" + formatNumber(nameindex) + ".twx.png";
                    var normalFile = new File(exportFolder + "/" + normalFilename);
                    doc.exportDocument(normalFile, ExportType.SAVEFORWEB, pngOpts);
                    nameindex++;
                    normalLayer.visible = false;
                } catch (saveError) {
                    alert("Error on save: " + saveError + "\n" + saveError.line);
                }

                for (var j = 0; j < layers.length; j++) {
                    layers[j].visible = false;
                }
            } else {
                alert("Layer '" + layerName + "'is not found.");
            }
        } catch (e) {
            alert("Layer '" + layerName + "' error: " + e);
        }
    }

    alert("All files exported successfully.");
}

try {
    exportLayersAsPNG();
} catch (e) {
    alert("Error: " + e + "\n" + e.line);
}
