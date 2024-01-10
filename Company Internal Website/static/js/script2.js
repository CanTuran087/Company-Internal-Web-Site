/*BIRTHDAY TABLE*/
const birthdayTable2 = $('#birthday-table-2').DataTable({
    paging: false,
    scrollCollapse: true,
    scrollY: '250px',
    info: false,
    searching: false,
    order: [[1, 'asc']],
    columnDefs: [
        {
            target: 3,
            visible: false,
            searchable: false
        },
        {
            target: 4,
            visible: false,
            searchable: false
        },
        {
            target: 5,
            visible: false,
            searchable: false
        }
    ],
});

/*CLICK*/
const imgColumnIndex0 = 0;
const imgColumnIndex1 = 1;
const imgColumnIndex2 = 2;
const imgColumnIndex3 = 3;
const imgColumnIndex4 = 4;
const imgColumnIndex5 = 5;

const nameInput = document.getElementById("name-input");
const dayInput = document.getElementById("day-input");
const birthdayInput = document.getElementById("birthday-input");
const ageInput = document.getElementById("age-input");
const emailInput = document.getElementById("email-input");

/*BIRTHDAY FIREWORK*/
function getRandomColor() {
    const letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}

function createFirework() {
    const firework = document.createElement('div');
    firework.className = 'firework2';
    firework.style.backgroundColor = getRandomColor();
    document.getElementById('fireworks-container').appendChild(firework);

    const randomX = Math.random() * window.innerWidth;
    const randomY = Math.random() * window.innerHeight;

    firework.style.left = `${randomX}px`;
    firework.style.top = `${randomY}px`;
}
/*BIRTHDAY FIREWORK*/

birthdayTable2.on('click', 'tbody tr', function () {
    const data = birthdayTable2.row(this).data();

    let imgSrc = data[imgColumnIndex5];
    imgSrc = imgSrc.replace(/<\/?p>/g, '');

    if (imgSrc == "") {
        $('#birthday-card-img').attr('src', "static/img/imgSRC.jpg");
    } else {
        $('#birthday-card-img').attr('src', imgSrc);
    }


    nameInput.value = data[imgColumnIndex0].replace(/<\/?p>/g, '');
    dayInput.value = data[imgColumnIndex1].replace(/<\/?p>/g, '');

    if (dayInput.value.slice(0, 5) === "     ") {
        dayInput.value = "Bugün Doğum Günü";

        document.getElementById('fireworks-container').style.display = 'flex';
        var container = document.getElementById('fireworks-container');

        while (container.firstChild) {
            container.removeChild(container.firstChild);
        }

        setInterval(createFirework, 800);
    } else {
        document.getElementById('fireworks-container').style.display = 'none';
    }

    birthdayInput.value = data[imgColumnIndex3].replace(/<\/?p>/g, '');
    ageInput.value = data[imgColumnIndex2].replace(/<\/?p>/g, '');
    emailInput.value = data[imgColumnIndex4].replace(/<\/?p>/g, '');
});
/*CLICK*/

/*SELECTED*/
birthdayTable2.on('click', 'tbody tr', (e) => {
    let classList = e.currentTarget.classList;

    if (classList.contains('selected')) {
        classList.remove('selected');

        $('#birthday-card-img').attr('src', "static/img/imgSRC.jpg");
        nameInput.value = "";
        dayInput.value = "";
        birthdayInput.value = "";
        ageInput.value = "";
        emailInput.value = "";
    }
    else {
        birthdayTable2.rows('.selected').nodes().each((row) => row.classList.remove('selected'));
        classList.add('selected');
    }
});
/*SELECTED*/
/*BIRTHDAY TABLE*/

/*MAIL TEXT EDITOR*/
var toolbarOptions = [
    ['bold', 'italic', 'underline', 'strike'],        // toggled buttons
    //['blockquote', 'code-block'],

    //[{ 'header': 1 }, { 'header': 2 }],               // custom button values
    [{ 'list': 'ordered' }, { 'list': 'bullet' }],
    //[{ 'script': 'sub'}, { 'script': 'super' }],      // superscript/subscript
    //[{ 'indent': '-1'}, { 'indent': '+1' }],          // outdent/indent
    //[{ 'direction': 'rtl' }],                         // text direction

    [{ 'size': ['small', false, 'large', 'huge'] }],  // custom dropdown
    //[{ 'header': [1, 2, 3, 4, 5, 6, false] }],

    [{ 'color': [] }, { 'background': [] }],          // dropdown with defaults from theme
    [{ 'font': [] }],
    [{ 'align': [] }],

    ['clean']                                         // remove formatting button
];

var quill = new Quill('#birthday-card-editor', {
    modules: {
        toolbar: toolbarOptions
    },
    theme: 'snow'
});
/*MAIL TEXT EDITOR*/

/*MAIL TEXT BUTTON*/
const birthdayMailButton = document.getElementById("birthday-mail-button");
const mailClickButton = document.getElementById("mail-a");

function isEmailValid(email) {
    const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
    return emailPattern.test(email);
}

birthdayMailButton.addEventListener("click", () => {
    var mailText = quill.root.innerHTML;
    mailText = mailText.replace(/<\/?p>/g, '');

    if (emailInput.value == "") {
        alertDialog("E-Mail Alanını Doldurunuz !", "error");
        return;
    }

    if (mailText == "<p><br></p>" || mailText == "" || mailText == "<br>") {
        alertDialog("Mail Text Alanını Doldurunuz !", "error");
        return;
    }

    if (isEmailValid(emailInput.value)) {
        var plainTextContent = quill.getText();
        mailClickButton.href = 'mailto:' + emailInput.value + '?subject=Doğum Günü&body=' + encodeURIComponent(plainTextContent);
        mailClickButton.click();
    } else {
        alertDialog("Lütfen geçerli bir e-posta adresi giriniz !", "error");
    }

});
/*MAIL TEXT BUTTON*/