const saveButton = document.getElementById("save");
const deleteCheck = document.getElementById("delete-checkbox");
let check, saved;

saved = 0;

deleteCheck.addEventListener("change", () => {
    if (deleteCheck.checked) {
        check = "okey";
    } else {
        check = "0";
    }
})

saveButton.addEventListener("click", (event) => {
    event.preventDefault();

    let textParagraphAbout = quill2.root.innerHTML;
    let textParagraphAnnouncement = quill3.root.innerHTML;
    let textParagraphManagementAnnouncement = quill4.root.innerHTML;

    textParagraphAbout = textParagraphAbout.replace(/<\/?p>/g, '');
    textParagraphAnnouncement = textParagraphAnnouncement.replace(/<\/?p>/g, '');
    textParagraphManagementAnnouncement = textParagraphManagementAnnouncement.replace(/<\/?p>/g, '');

    if (check == "okey") {
        if (liElement.innerHTML === '<i class="fa-solid fa-moon"></i>') {
            background = "white";
            color = 'black';
        } else {
            background = "black";
            color = 'white';
        }

        Swal.fire({
            title: "Silindi Tiki İşaretli",
            text: "Silindi tiki işaretli, seçili duyurular silinecektir. Emin misiniz ?",
            icon: "warning",
            showCancelButton: true,
            confirmButtonColor: "#3085d6",
            cancelButtonColor: "#d33",
            confirmButtonText: "Sil",
            cancelButtonText: "Çık",
            background: background,
            color: color
        }).then((result) => {
            if (result.isConfirmed) {
                if ((filePath.value != ''
                    || filePath2.value != ''
                    || filePath3.value != ''
                    || filePath4.value != ''
                    || (tableIdInput.value != "" && filePath5.value != '')
                    || (textParagraphAbout != '' && textParagraphAbout != '<br>')
                    || (textParagraphAnnouncement != '' && textParagraphAnnouncement != '<br>')
                    || (tableIdInput.value != "" && textParagraphManagementAnnouncement != '' && textParagraphManagementAnnouncement != '<br>'))
                    && (tableIdInput.value != "" && check === "okey")) {
                    alertDialog("Değişiklikler Kaydedildi", "success");
                    fetch("/managementAnnouncement", {
                        method: "POST",
                        body: JSON.stringify
                            ({
                                base64img: base64img,
                                filePath: filePath.value,
                                base64img2: base64img2,
                                filePath2: filePath2.value,
                                base64img3: base64img3,
                                filePath3: filePath3.value,
                                base64img4: base64img4,
                                filePath4: filePath4.value,
                                base64img5: base64img5,
                                filePath5: filePath5.value,
                                textParagraphAbout: textParagraphAbout,
                                textParagraphAnnouncement: textParagraphAnnouncement,
                                textParagraphManagementAnnouncement: textParagraphManagementAnnouncement,
                                tableIdInput: tableIdInput.value,
                                check: check,
                                employee: employeeSelect.value.split(" - ")[0],
                                employeeUserName: userName.value
                            }),

                        headers: {
                            "Content-Type": "application/json"
                        }
                    })
                        .then((response) => {
                            response.json()
                            setTimeout(function () {
                                window.location.reload();
                            }, 1000);
                        }
                        )
                        .then(data => {
                            console.log("Sunucu Yanıtı", data);
                        })
                        .catch(error => {
                            console.error("Hata:", error);
                        })
                }
                else if (tableIdInput.value != "" && check === "okey") {
                    alertDialog("Değişiklikler Kaydedildi", "success");
                    fetch("/managementAnnouncement", {
                        method: "POST",
                        body: JSON.stringify
                            ({
                                tableIdInput: tableIdInput.value,
                                check: check
                            }),

                        headers: {
                            "Content-Type": "application/json"
                        }
                    })
                        .then((response) => {
                            response.json();
                            setTimeout(function () {
                                window.location.reload();
                            }, 1000);
                        }
                        )
                        .then(data => {
                            console.log("Sunucu Yanıtı", data);
                        })
                        .catch(error => {
                            console.error("Hata:", error);
                        })
                }
            }
        });
    }
    if (filePath.value != ''
        || filePath2.value != ''
        || filePath3.value != ''
        || filePath4.value != ''
        || (tableIdInput.value != "" && filePath5.value != '')
        || (textParagraphAbout != '' && textParagraphAbout != '<br>')
        || (textParagraphAnnouncement != '' && textParagraphAnnouncement != '<br>')
        || (tableIdInput.value != "" && textParagraphManagementAnnouncement != '' && textParagraphManagementAnnouncement != '<br>')) {
        alertDialog("Değişiklikler Kaydedildi", "success");
        fetch("/managementAnnouncement", {
            method: "POST",
            body: JSON.stringify
                ({
                    base64img: base64img,
                    filePath: filePath.value,
                    base64img2: base64img2,
                    filePath2: filePath2.value,
                    base64img3: base64img3,
                    filePath3: filePath3.value,
                    base64img4: base64img4,
                    filePath4: filePath4.value,
                    base64img5: base64img5,
                    filePath5: filePath5.value,
                    textParagraphAbout: textParagraphAbout,
                    textParagraphAnnouncement: textParagraphAnnouncement,
                    textParagraphManagementAnnouncement: textParagraphManagementAnnouncement,
                    tableIdInput: tableIdInput.value,
                    check: check,
                    employee: employeeSelect.value.split(" - ")[0],
                    employeeUserName: userName.value
                }),
            headers: {
                "Content-Type": "application/json"
            }
        })
            .then((response) => {
                response.json()
                setTimeout(function () {
                    window.location.reload();
                }, 1000);
            }
            )
            .then(data => {
                console.log("Sunucu Yanıtı", data);
            })
            .catch(error => {
                console.error("Hata:", error);
            })
    } else {
        saved = 0;
    }

});