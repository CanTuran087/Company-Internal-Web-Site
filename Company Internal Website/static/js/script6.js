const saveDetailButton = document.getElementById("saveDetail");

saveDetailButton.addEventListener("click", (event) => {
    event.preventDefault();

    let textParagraphAnnouncementDetail = quill5.root.innerHTML;
    textParagraphAnnouncementDetail = textParagraphAnnouncementDetail.replace(/<\/?p>/g, '');

    if (textParagraphAnnouncementDetail === ""
        || textParagraphAnnouncementDetail === "<br>") {
        alertDialog("Lütfen Detay Yazısını Doldurunuz !", "error");
    }

    else if (filePath6.value === "") {
        alertDialog("Lütfen Detay Yazısı İçin Resim Ekleyiniz !", "error");
    }

    else {
        alertDialog("Değişiklikler Kaydedildi", "success");
        fetch("/managementAnnouncementDetailSave", {
            method: "POST",
            body: JSON.stringify
                ({
                    base64img6: base64img6,
                    filePath6: filePath6.value,
                    textParagraphAnnouncementDetail: textParagraphAnnouncementDetail,
                    localIMGSrc: localIMGSrc,
                    localFilePath: localFilePath,
                    localParagraph: localParagraph,
                    localAnnouncementID: localAnnouncementID
                }),

            headers: {
                "Content-Type": "application/json"
            }
        })
            .then(response => response.json())
            .then(data => {
                console.log("Sunucu Yanıtı", data);
            })
            .catch(error => {
                console.error("Hata:", error);
            })
    }
});