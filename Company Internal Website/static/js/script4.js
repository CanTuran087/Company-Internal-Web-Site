/*LOCALSTORAGE GET DATA*/
const localIMGSrc = localStorage.getItem("localIMGSrc");
const localParagraph = localStorage.getItem("localParagraph");
const localFilePath = localStorage.getItem("localFilePath");
const localAnnouncementID = localStorage.getItem("localAnnouncementID");

console.log(localAnnouncementID);
document.getElementById("summary-announcement-img").src = localIMGSrc;

document.addEventListener("DOMContentLoaded", () => {
    document.getElementById('summary-announcement').textContent = localParagraph;
})
/*LOCALSTORAGE GET DATA*/

/*ANNOUNCEMENT DETAIL TEXT EDITOR*/
var toolbarOptions2 = [
    ['bold', 'italic', 'underline'],
    ['clean']
];

var quill5 = new Quill('#announcement-card-detail-editor', {
    modules: {
        toolbar: toolbarOptions2
    },
    theme: 'snow',
    placeholder: 'Duyurular için detay yazısı giriniz...',
});
/*ANNOUNCEMENT DETAIL TEXT EDITOR*/

/*DOSYA SEÇME, DOSYA İSMİNİ ALMA VE BASE64 FORMATINA DÖNÜŞTÜRME*/
const fileInput6 = document.getElementById("fileInput-6");
const fileSelectButton6 = document.getElementById("file-selectButton-6");
const filePath6 = document.getElementById("filePath-6");
let base64img6 = "";

fileSelectButton6.addEventListener("click", () => {
    fileInput6.click();
});

fileInput6.addEventListener("change", () => {
    if (fileInput6.files.length > 0) {
        const selectedFile6 = fileInput6.files[0];

        if (selectedFile6) {
            const fileName6 = selectedFile6.name;

            if (fileName6.slice(-4) == ".jpg" || fileName6.slice(-4) == ".png" || fileName6.slice(-5) == ".jpeg") {
                filePath6.value = fileName6;
                const fileReader6 = new FileReader();
                fileReader6.readAsDataURL(selectedFile6);
                fileReader6.onload = () => {
                    base64img6 = fileReader6.result;
                    $('#announcement-card-detail-img').attr('src', fileReader6.result);
                }
            } else {
                alertDialog("Lütfen jpg veya png Formatında Dosya Seçiniz", "error");
            }
        }

    }
});

const deleteButton6 = document.getElementById("delete-button-6");
deleteButton6.addEventListener("click", () => {
    filePath6.value = "";
    $('#announcement-card-detail-img').attr('src', "static/img/imgSRC.jpg");
});
/*DOSYA SEÇME, DOSYA İSMİNİ ALMA VE BASE64 FORMATINA DÖNÜŞTÜRME*/