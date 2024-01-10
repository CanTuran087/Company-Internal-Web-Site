let globalID;

function globalVeriable(veriable) {
    globalID = veriable;
}


const announcementDetailButton = document.querySelector('.announcement-detail-button-a');

announcementDetailButton.addEventListener('click', () => {

    fetch("/ShowAnnouncementDetail", {
        method: "POST",
        body: JSON.stringify({
            globalID: globalID
        }),
        headers: {
            "Content-Type": "application/json"
        }
    })
        .then((response)=>{
                response.json()
                window.location.href = "/announcement-detail";
            }
        )
        .then(data => {
            console.log("Sunucu Yanıtı", data);
        })
        .catch(error => {
            console.error("Hata:", error);
        });
});