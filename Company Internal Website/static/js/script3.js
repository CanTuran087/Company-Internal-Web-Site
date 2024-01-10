/*DOSYA SEÇME, DOSYA İSMİNİ ALMA VE BASE64 FORMATINA DÖNÜŞTÜRME*/
const form = document.querySelector('form');
const fileInput = document.getElementById("fileInput");
const fileSelectButton = document.getElementById("file-selectButton");
const filePath = document.getElementById("filePath");
let base64img = "";

fileSelectButton.addEventListener("click", () => {
    fileInput.click();
});

fileInput.addEventListener("change", () => {
    if (fileInput.files.length > 0) {
        const selectedFile = fileInput.files[0];

        if (selectedFile) {
            const fileName = selectedFile.name;

            if (fileName.slice(-4) == ".jpg" || fileName.slice(-4) == ".png" || fileName.slice(-5) == ".jpeg") {
                filePath.value = fileName;
                const fileReader = new FileReader();
                fileReader.readAsDataURL(selectedFile);
                fileReader.onload = () => {
                    base64img = fileReader.result;
                }
            } else {
                alertDialog("Lütfen jpg veya png Formatında Dosya Seçiniz", "error");
            }
        }

    }
});

const fileInput2 = document.getElementById("fileInput-2");
const fileSelectButton2 = document.getElementById("file-selectButton-2");
const filePath2 = document.getElementById("filePath-2");
const employeeSelect = document.getElementById("employee-select");
let base64img2 = "";

fileSelectButton2.addEventListener("click", () => {
    const selectedEmployee = employeeSelect.value;

    if (selectedEmployee == "Çalışan Seçiniz") {
        alertDialog("Lütfen İlgili Çalışanı Seçiniz", "error");
    } else {
        fileInput2.click();
    }
});

fileInput2.addEventListener("change", () => {
    if (fileInput2.files.length > 0) {
        const selectedFile2 = fileInput2.files[0];

        if (selectedFile2) {
            const fileName2 = selectedFile2.name;

            if (fileName2.slice(-4) == ".jpg" || fileName2.slice(-4) == ".png" || fileName2.slice(-5) == ".jpeg") {
                filePath2.value = fileName2;
                const fileReader2 = new FileReader();
                fileReader2.readAsDataURL(selectedFile2);
                fileReader2.onload = () => {
                    base64img2 = fileReader2.result;
                    console.log(fileReader2.result);
                    $('#employee-file-img').attr('src', fileReader2.result);
                }
            } else {
                alertDialog("Lütfen jpg veya png Formatında Dosya Seçiniz", "error");
            }
        }

    }
});

const fileInput3 = document.getElementById("fileInput-3");
const fileSelectButton3 = document.getElementById("file-selectButton-3");
const filePath3 = document.getElementById("filePath-3");
let base64img3 = "";

fileSelectButton3.addEventListener("click", () => {
    fileInput3.click();
});

fileInput3.addEventListener("change", () => {
    if (fileInput3.files.length > 0) {
        const selectedFile3 = fileInput3.files[0];

        if (selectedFile3) {
            const fileName3 = selectedFile3.name;

            if (fileName3.slice(-4) == ".jpg" || fileName3.slice(-4) == ".png" || fileName3.slice(-5) == ".jpeg") {
                filePath3.value = fileName3;
                const fileReader3 = new FileReader();
                fileReader3.readAsDataURL(selectedFile3);
                fileReader3.onload = () => {
                    base64img3 = fileReader3.result;
                    $('#about-file-img').attr('src', fileReader3.result);
                }
            } else {
                alertDialog("Lütfen jpg veya png Formatında Dosya Seçiniz", "error");
            }
        }

    }
});

const fileInput4 = document.getElementById("fileInput-4");
const fileSelectButton4 = document.getElementById("file-selectButton-4");
const filePath4 = document.getElementById("filePath-4");
let base64img4 = "";

fileSelectButton4.addEventListener("click", () => {
    fileInput4.click();
});

fileInput4.addEventListener("change", () => {
    if (fileInput4.files.length > 0) {
        const selectedFile4 = fileInput4.files[0];

        if (selectedFile4) {
            const fileName4 = selectedFile4.name;

            if (fileName4.slice(-4) == ".jpg" || fileName4.slice(-4) == ".png" || fileName4.slice(-5) == ".jpeg") {
                filePath4.value = fileName4;
                const fileReader4 = new FileReader();
                fileReader4.readAsDataURL(selectedFile4);
                fileReader4.onload = () => {
                    base64img4 = fileReader4.result;
                    $('#announcement-file-img').attr('src', fileReader4.result);
                }
            } else {
                alertDialog("Lütfen jpg veya png Formatında Dosya Seçiniz", "error");
            }
        }

    }
});

const fileInput5 = document.getElementById("fileInput-5");
const fileSelectButton5 = document.getElementById("file-selectButton-5");
const filePath5 = document.getElementById("filePath-5");
let base64img5 = "";

fileSelectButton5.addEventListener("click", () => {
    fileInput5.click();
});

fileInput5.addEventListener("change", () => {
    if (fileInput5.files.length > 0) {
        const selectedFile5 = fileInput5.files[0];

        if (selectedFile5) {
            const fileName5 = selectedFile5.name;

            if (fileName5.slice(-4) == ".jpg" || fileName5.slice(-4) == ".png" || fileName5.slice(-5) == ".jpeg") {
                filePath5.value = fileName5;
                const fileReader5 = new FileReader();
                fileReader5.readAsDataURL(selectedFile5);
                fileReader5.onload = () => {
                    base64img5 = fileReader5.result;
                }
            } else {
                alertDialog("Lütfen jpg veya png Formatında Dosya Seçiniz", "error");
            }
        }

    }
});
/*DOSYA SEÇME, DOSYA İSMİNİ ALMA VE BASE64 FORMATINA DÖNÜŞTÜRME*/


/*TEXT EDITOR*/
var toolbarOptions2 = [
    ['bold', 'italic', 'underline'],
    ['clean']
];

/*ABOUT TEXT EDITOR*/
var quill2 = new Quill('#about-card-editor', {
    modules: {
        toolbar: toolbarOptions2
    },
    theme: 'snow',
    placeholder: 'Hakkımızda sekmesi için metin giriniz...',
});
/*ABOUT TEXT EDITOR*/

/*ANNOUNCEMENT TEXT EDITOR*/
var quill3 = new Quill('#announcement-card-editor', {
    modules: {
        toolbar: toolbarOptions2
    },
    theme: 'snow',
    placeholder: 'Duyurular için özet yazı giriniz...',
});
/*ANNOUNCEMENT TEXT EDITOR*/

/*MANAGEMENT ANNOUNCEMENT TEXT EDITOR*/
var quill4 = new Quill('#management-announcement-editor', {
    modules: {
        toolbar: toolbarOptions2
    },
    theme: 'snow',
    placeholder: 'Yeni özet yazıyı giriniz...',
});
/*MANAGEMENT ANNOUNCEMENT TEXT EDITOR*/

/*TEXT EDITOR*/


/*DELETE BUTTON*/
const deleteButton = document.getElementById("delete-button");
deleteButton.addEventListener("click", () => {
    filePath.value = "";
});

const deleteButton2 = document.getElementById("delete-button-2");
deleteButton2.addEventListener("click", () => {
    filePath2.value = "";
    $('#employee-file-img').attr('src', "static/img/imgSRC.jpg");
});

const deleteButton3 = document.getElementById("delete-button-3");
deleteButton3.addEventListener("click", () => {
    filePath3.value = "";
    $('#about-file-img').attr('src', "static/img/imgSRC.jpg");
});

const deleteButton4 = document.getElementById("delete-button-4");
deleteButton4.addEventListener("click", () => {
    filePath4.value = "";
    $('#announcement-file-img').attr('src', "static/img/imgSRC.jpg");
});

const deleteButton5 = document.getElementById("delete-button-5");
deleteButton5.addEventListener("click", () => {
    filePath5.value = "";
});
/*DELETE BUTTON*/


/*MANAGEMENT ANNOUNCEMENT TABLE*/
const managementAnnouncementTable = $('#management-announcement-table').DataTable({
    paging: false,
    scrollCollapse: true,
    scrollY: '194px',
    info: false,
    searching: false,
    columnDefs: [
        {
            target: [0, 4, 5, 6],
            visible: false,
            searchable: false
        },
        { "width": "40%", "targets": 1 },
        { "width": "30%", "targets": 2 },
        { "width": "30%", "targets": 3 }
    ],
});

/*CLICK*/
const tableColumnIndex = [0, 1, 2, 3, 4, 5, 6];

const tableIdInput = document.getElementById("table-id");
const tableFileNameInput = document.getElementById("table-fileName");
const tableCreatedBy = document.getElementById("table-CreatedBy");
const tableCreatedAt = document.getElementById("table-CreatedAt");
let announcementText, announcementID;

managementAnnouncementTable.on('click', 'tbody tr', function () {
    const data = managementAnnouncementTable.row(this).data();

    let imgSrc = data[tableColumnIndex[6]];
    imgSrc = imgSrc.replace(/<\/?p>/g, '');
    $('#management-announcement-table-img').attr('src', imgSrc);

    tableIdInput.value = data[tableColumnIndex[0]].replace(/<\/?p>/g, '');
    announcementText = data[tableColumnIndex[1]].replace(/<\/?p>/g, '');
    tableFileNameInput.value = data[tableColumnIndex[2]].replace(/<\/?p>/g, '');
    tableCreatedBy.value = data[tableColumnIndex[4]].replace(/<\/?p>/g, '');
    tableCreatedAt.value = data[tableColumnIndex[5]].replace(/<\/?p>/g, '');
});
/*CLICK*/

/*SELECTED*/
managementAnnouncementTable.on('click', 'tbody tr', (e) => {
    let classList = e.currentTarget.classList;

    if (classList.contains('selected')) {
        classList.remove('selected');

        $('#management-announcement-table-img').attr('src', "static/img/imgSRC.jpg");
        tableIdInput.value = "";
        tableFileNameInput.value = "";
        tableCreatedBy.value = "";
        tableCreatedAt.value = "";
    }
    else {
        managementAnnouncementTable.rows('.selected').nodes().each((row) => row.classList.remove('selected'));
        classList.add('selected');
    }
});
/*SELECTED*/
/*MANAGEMENT ANNOUNCEMENT TABLE*/

/*CONTROL*/
const detailButtonSummaryExists = document.querySelector(".announcement-detail-button-summary-exists");
const detailButtonSelected = document.querySelector(".announcement-detail-button-selected");

document.addEventListener("DOMContentLoaded", function () {
    const textEditorParagraph = document.querySelector("#announcement-card-editor .ql-blank p");

    detailButtonSummaryExists.addEventListener("click", () => {
        if (filePath4.value == "") {
            alertDialog("Lütfen Duyuru Resmi Giriniz !", "error");
        } else {
            if (textEditorParagraph && (textEditorParagraph.innerText.trim() !== "")) {
                const localIMGSrc = document.getElementById('announcement-file-img').src;
                const localParagraph = textEditorParagraph.innerText;
                localStorage.setItem('localIMGSrc', localIMGSrc);
                localStorage.setItem('localParagraph', localParagraph);
                localStorage.setItem('localFilePath', filePath4.value);
                localStorage.setItem('localAnnouncementID', "");

                fetch("/managementAnnouncementDetailButton", {
                    method: "POST",
                    body: JSON.stringify
                        ({
                            localAnnouncementID: ""
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
                window.open('management-announcement-detail')
                //window.location.href = 'management-announcement-detail';
            } else {
                alertDialog("Lütfen Özet Duyuru Yazısı Giriniz !", "error");
            }
        }
    });
});

detailButtonSelected.addEventListener("click", () => {
    if (tableIdInput.value == "" || tableIdInput.value == "ID") {
        alertDialog("Lütfen İlgili Duyuruyu Seçiniz !", "error");
    } else {
        const localIMGSrc = document.getElementById('management-announcement-table-img').src;
        localStorage.setItem('localIMGSrc', localIMGSrc);
        localStorage.setItem('localParagraph', announcementText);
        localStorage.setItem('localFilePath', tableFileNameInput.value);
        announcementID = tableIdInput.value;
        localStorage.setItem('localAnnouncementID', announcementID);

        fetch("/managementAnnouncementDetailButton", {
            method: "POST",
            body: JSON.stringify
                ({
                    localAnnouncementID: announcementID
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
        window.open('management-announcement-detail');
    }
})
/*CONTROL*/

/*SELECTED USERNAME*/
const userName = document.getElementById('userName');
employeeSelect.addEventListener("click", () => {
    userName.value = employeeSelect.value.split(" - ")[1];

    if (userName.value == "undefined") {
        userName.value = "";
    }
})
/*SELECTED USERNAME*/