/*NAVBAR BUTTON*/
const bars = document.getElementById("nav-action");
const nav = document.getElementById("nav");

bars.addEventListener("click", () => {
  bars.classList.toggle('active');
  nav.classList.toggle('visible');
}, false);
/*NAVBAR BUTTON*/

/*BUGÜN DOĞUM GÜNÜ OLANLARIN YANINDA SÜREKLİ HAVA FİŞEK GÖSTERİP GİZLER*/
document.addEventListener("DOMContentLoaded", () => {
  var fireworks = document.querySelectorAll(".firework");
  fireworks.forEach((firework) => {
      setTimeout(() => {
          firework.classList.remove("hidden");
          firework.classList.add("animated");
      }, 1000);
  });
})
/*BUGÜN DOĞUM GÜNÜ OLANLARIN YANINDA SÜREKLİ HAVA FİŞEK GÖSTERİP GİZLER*/

/*DARK - LIGHT THEME*/
const liElement = document.querySelector("li.dark-light-theme");
const cards = document.querySelector(".cards");
const body = document.querySelector("body");
liElement.innerHTML = '<i class="fa-solid fa-moon"></i>';

liElement.addEventListener("click", () => {
    if (liElement.innerHTML == '<i class="fa-solid fa-moon"></i>') {
        liElement.innerHTML = '<i class="fa-solid fa-sun"></i>';
        cards.classList.toggle("clicked");
        cards.classList.remove("clicked2");
        body.classList.toggle("clicked");
        body.classList.remove("clicked2");
    } else{
        liElement.innerHTML = '<i class="fa-solid fa-moon"></i>';
        cards.classList.toggle("clicked2");
        cards.classList.remove("clicked");
        body.classList.toggle("clicked2");
        body.classList.remove("clicked");
    }
})
/*DARK - LIGHT THEME*/

/*ALERT*/
const alertDialog = (message, icon) => {
  let background, color;

  if (liElement.innerHTML === '<i class="fa-solid fa-moon"></i>') {
    background = "white";
    color = 'black';
  } else{
    background = "black";
    color = 'white';
  }

  Swal.fire({
    position: 'center',
    icon: icon,
    title: message,
    showConfirmButton: false,
    timer: 1500,
    background: background,
    color: color
  });
}
/*ALERT*/

/*BIRTHDAY DATATABLE*/
new DataTable('#birthday-table', {
  paging: false,
  scrollCollapse: true,
  scrollY: '200px',
  info: false,
  searching: false,
  order: [[1, 'asc']]
});
/*BIRTHDAY DATATABLE*/


/*IMG SLIDER*/
var announcementDetailID; 

document.addEventListener('DOMContentLoaded', () => {
  new Splide('#image-slider', {
    type: 'loop',
    perPage: 1,
    pagination: true,
    autoplay: true,
    interval: 4000,
  }).mount();

  let announcementDetailIDInputs = document.querySelectorAll('.splide__slide input[name="announcement-ID"]:not([tabindex="-1"])');

  setInterval(() => {
    announcementDetailIDInputs = document.querySelectorAll('.splide__slide input[name="announcement-ID"]:not([tabindex="-1"])');

    if (announcementDetailIDInputs.length > 0) {
      announcementDetailID = announcementDetailIDInputs[0].value;
      globalVeriable(announcementDetailID);
    }
  }, 500);
});
/*IMG SLIDER*/


/*SCROLL BUTTON*/
const scrollButton = document.getElementById("scroll-to-top");

window.addEventListener("load", () => {

  window.addEventListener("scroll", () => {
    if (window.pageYOffset > 100) {
      scrollButton.classList.remove("arrow-button-hidden");
    } else {
      scrollButton.classList.add("arrow-button-hidden");
    }
  });

  scrollButton.addEventListener("click", () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  });

});
/*SCROLL BUTTON*/


/*SELECTED PLANT*/
const plantSelect = document.getElementById("plant-select");
const sectionSelect = document.getElementById("section-select");
const companySelect = document.getElementById("company-select");
const employeeCompanyLogo = document.getElementById("employee-company-logo");
let imgURL;
imgURL = "";

companySelect.addEventListener("change", () => {
  if (companySelect.value === "Seçiniz") {
    alertDialog("Lütfen Firma Seçiniz !", "error");
    plantSelect.innerHTML = "";
  } else {
    plantSelect.innerHTML = "";
    var options = ["Seçiniz", "Tesis1", "Tesis2"];

    for (let i = 0; i < options.length; i++) {
      let option = document.createElement("option");
      option.text = options[i];
      plantSelect.add(option);
    }

    /*IMG SELECTED BY COMPANY*/
    if (companySelect.value === "Company1") {
      imgURL = "static/img/company1Logo.jpg";
    } else if (companySelect.value === "Company2") {
      imgURL = "static/img/company2Logo.jpg";
    } else {
      imgURL = "static/img/company3Logo.jpg";
    }

    employeeCompanyLogo.src = imgURL;
    employeeCompanyLogo.alt = companySelect.value;
    /*IMG SELECTED BY COMPANY*/
  }
});

updateSections = () => {
  const selectedPlant = plantSelect.value;
  var options = [];

  if (selectedPlant === "Tesis1") {
    sectionSelect.innerHTML = "";
    options = ['Seçiniz', 'Seçenek1','Seçenek2','Seçenek3','Seçenek4'];
  } else if (selectedPlant === "Tesis2") {
    sectionSelect.innerHTML = "";
    options = ['Seçiniz', 'Seçenek1','Seçenek2','Seçenek3','Seçenek4'];
  } else {
    alertDialog("Lütfen Tesis Seçiniz !", "error");
    sectionSelect.innerHTML = "";
  }


  for (let i = 0; i < options.length; i++) {
    let option = document.createElement("option");
    option.text = options[i];
    sectionSelect.add(option);
  }
};

plantSelect.addEventListener("change", updateSections);
/*SELECTED PLANT*/


/*EMPLOYEE DATATABLE*/
const employeeDataTable = $('#employee-table').DataTable({
  paging: false,
  scrollCollapse: true,
  scrollY: '150px',
  info: false,
  searching: true,
  language: {
    search: "",
    searchPlaceholder: "Global Arama"
  },
  dom: 'Bfrtip',
  buttons: [
    {
      extend: 'pdf',
      text: '<i class="fas fa-file-pdf" style="font-size: 140%;"></i>',
      titleAttr: 'PDF'
    },
    {
      extend: 'excel',
      text: '<i class="fas fa-file-excel" style="font-size: 140%;"></i>',
      titleAttr: 'EXCEL',
    },
    {
      extend: 'copy',
      text: '<i class="fas fa-clone" style="font-size: 140%;"></i>',
      titleAttr: 'COPY',
    },
  ]
});

arrowButtonEmployee = document.querySelector(".arrow-button-employee button");
const employeeTable = $('#employee-table').DataTable();

arrowButtonEmployee.addEventListener("click", () => {

  const selectedCompanyFilter = companySelect.value.slice(0, 3);
  const selectedPlantFilter = plantSelect.value.slice(0, 3);
  const selectedSectionFilter = sectionSelect.value.slice(0, 3);

  if (selectedCompanyFilter != "" && selectedCompanyFilter != "Seç") {
    employeeTable.column(1).search(selectedCompanyFilter).draw();
  } else {
    employeeTable.column(1).search("").draw();
  }

  if (selectedPlantFilter != "" && selectedPlantFilter != "Seç") {
    employeeTable.column(2).search(selectedPlantFilter).draw();
  } else {
    employeeTable.column(2).search("").draw();
  }

  if (selectedSectionFilter != "" && selectedSectionFilter != "Seç") {
    employeeTable.column(3).search(selectedSectionFilter).draw();
  } else {
    employeeTable.column(3).search("").draw();
  }
});
/*EMPLOYEE DATATABLE*/

/*CONTACT HIDDEN TEXT*/
const button = document.querySelectorAll(".envelope-link, .linkedin-link, .youtube-link, .instagram-link, .instagram-link");

button.addEventListener("mouseover", mouseoverText());
button.addEventListener("mouseleave", mouseleaveText());

const mouseoverText = () => {
  if ($(".hidden-text").first().is(":hidden")) {
    $(".hidden-text").show("");
  } else {
    $(".hidden-text").slideUp();
  }
}

const mouseleaveText = () => {
  if ($(".hidden-text").first().is(":hidden")) {
    $(".hidden-text").slideUp();
  } else {
    $(".hidden-text").show("slow");
  }
}
/*CONTACT HIDDEN TEXT*/