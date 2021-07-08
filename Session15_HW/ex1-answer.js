const $ulElement = document.querySelector("ul");

$ulElement.addEventListener("click", (e) => {
  const $target = e.target;
  if ($target.classList.contains("close")) {
    const $parentTarget = $target.parentElement;
    $parentTarget.style.display = "none";
    console.dir($parentTarget);
    const deleteItem = $parentTarget.childNodes[1].innerText;
    deleteTodoList("todoList", deleteItem);
  }
  $target.classList.toggle("checked");
});

function newElement() {
  const inputValue = document.getElementById("myInput").value;
  const $liElement = `
        <li>
            <span>${inputValue}</span>
            <span class="close">&#215;</span>
        </li>
    `;

  if (inputValue === "") {
    alert("You must write something!");
  } else {
    $ulElement.insertAdjacentHTML("beforeend", $liElement);
    addTodoList("todoList", inputValue);
  }
  document.getElementById("myInput").value = "";
}

function init() {
  let todoList = getTodoList("todoList");
  for (let i = 0; i < todoList.length; i++) {
    $liElement = `
            <li>
                ${todoList[i]}
                <span class="close">&#215;</span>
            </li>
        `;
    $ulElement.insertAdjacentHTML("beforeend", $liElement);
  }
}

function getTodoList(key) {
  return localStorage.getItem(key) ? localStorage.getItem(key).split(",") : [];
}

function addTodoList(key, value) {
  const todoList = getTodoList(key);
  return localStorage.setItem(key, [...todoList, value]);
}

function deleteTodoList(key, value) {
  const todoList = getTodoList(key);
  return localStorage.setItem(
    key,
    todoList.filter((todo) => todo !== value)
  );
}

init();

var i = 0;
function move() {
  if (i == 0) {
    i = 1;
    var elem = document.getElementById("myBar");
    var width = 1;
    var id = setInterval(frame, 10);
    function frame() {
      if (width >= 100) {
        clearInterval(id);
        i = 0;
      } else {
        width++;
        elem.style.width = width + "%";
      }
    }
  }
}

var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
btn.onclick = function () {
  modal.style.display = "block";
};

// When the user clicks on <span> (x), close the modal
span.onclick = function () {
  modal.style.display = "none";
};

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
};
