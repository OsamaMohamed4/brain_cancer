document.addEventListener("DOMContentLoaded", function(event) {
  var cont1Elements = document.querySelectorAll(".cont1");

  function checkScroll() {
    for (var i = 0; i < cont1Elements.length; i++) {
      var element = cont1Elements[i];
      var positionFromTop = element.getBoundingClientRect().top;

      if (positionFromTop - window.innerHeight <= 0) {
        element.classList.add("animate");
      }
    }
  }

  window.addEventListener("scroll", checkScroll);
  checkScroll();
});


function showChangePasswordForm() {
  var form = document.getElementById("change-password-form");
  form.style.display = "block";
  var form1 = document.getElementById("con");
  form1.style.display="none";
  var form1 = document.getElementById("Sign-form");
  form1.style.display="none";
}

function LoginForm() {
  var form = document.getElementById("change-password-form");
  form.style.display = "none";
  var form1 = document.getElementById("con");
  form1.style.display="block";
  var form1 = document.getElementById("Sign-form");
  form1.style.display="none";
}

function SignForm() {
  var form = document.getElementById("change-password-form");
  form.style.display = "none";
  var form1 = document.getElementById("con");
  form1.style.display="none";
  var form1 = document.getElementById("Sign-form");
  form1.style.display="block";
}


const label = document.querySelector('label');
const list = document.querySelector('#list');

label.addEventListener('mouseover', () => {
  list.style.display = 'block';
});

label.addEventListener('mouseout', () => {
  list.style.display = 'none';
});