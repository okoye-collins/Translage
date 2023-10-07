const TodoTask = document.querySelectorAll(".todo-task");
const DoneTask = document.querySelectorAll(".task-tag");
const Options = JSON.parse(
  document.getElementById("radioButtonsContainer").getAttribute("user_lan")
);
const TaskInput = document.querySelector(".task-translate");
const EditBtn = document.querySelectorAll(".edit-btn");
const DeleteBtn = document.querySelectorAll(".delete-btn");
const ColseModel = document.querySelector(".close-modal");
const DownloadBtn = document.querySelector('.download_btn')

console.log(DownloadBtn)

function createRadioButtons(options) {
  const container = document.getElementById("radioButtonsContainer");
  container.innerHTML = " ";
  // Loop through the options and create radio buttons
  for (let i = 0; i < options.length; i++) {
    const option = options[i];

    // Create the radio button input element
    const radioInput = document.createElement("input");
    radioInput.type = "radio";
    radioInput.id = "option" + i;
    radioInput.name = "options";
    radioInput.value = option;
    radioInput.style.color = "black";

    // Create the label for the radio button
    const radioLabel = document.createElement("label");
    radioLabel.htmlFor = "option" + i;
    radioLabel.textContent = option;
    radioLabel.style.color = "black";

    // Append the radio button and label to the container
    container.appendChild(radioInput);
    container.appendChild(radioLabel);

    // Add a line break to separate radio buttons
    container.appendChild(document.createElement("br"));
  }
}

TodoTask.forEach((task) => {
  task.addEventListener("click", () => {
    const ModalCard = document.querySelector(".modal-card");
    ModalCard.innerHTML = task.innerHTML;
    TaskInput.setAttribute("value", task.getAttribute("task_id"));
    // TaskInput.setAttribute('value', task.innerHTML.trim())
    createRadioButtons(Options);
  });
});

DoneTask.forEach((task) => {
  task.addEventListener("click", () => {
    const ModalCard = document.querySelector(".modal-card-done");
    const TaskDone_lan = document.querySelector(".done-task-lan");
    const TaskTranslateField = document.querySelector(".translated-field");
    const btn_edit = document.querySelector(".edit-btn");
    const btn_delete = document.querySelector(".delete-btn");
    ModalCard.innerHTML = task.innerHTML;
    TaskDone_lan.innerHTML = task.getAttribute("language");
    TaskTranslateField.value = task.getAttribute("translate");
    btn_edit.setAttribute("task_id", task.getAttribute("task_id"));
    btn_delete.setAttribute("task_id", task.getAttribute("task_id"));
  });
});

EditBtn.forEach((btn) => {
  btn.addEventListener("click", () => {
    if (btn.innerHTML.trim() === "EDIT") {
      btn.innerHTML = "UPDATE";
      const TaskTranslateField = document.querySelector(".translated-field");
      TaskTranslateField.removeAttribute("readonly");
    } else if (btn.innerHTML.trim() == "UPDATE") {
      btn.innerHTML = "EDIT";
      const TaskTranslateField = document.querySelector(".translated-field");
      TaskTranslateField.setAttribute("readonly", "readonly");
      // btn.removeAttribute('type')
      const EditForm = document.querySelector("#edit-form");
      const formData = new FormData(EditForm);

      fetch(`/edit_task/${btn.getAttribute("task_id")}/`, {
        method: "POST",
        body: formData,
      })
        .then((response) => {
          if (response.ok) {
            document.getElementById("myEditModal").close();
            location.reload();
          } else {
            console.log("an error occur");
          }
        })
        .catch((error) => {
          console.log(error);
        });
    }
  });
});

DeleteBtn.forEach((btn) => {
  btn.addEventListener("click", () => {
    if (btn.innerHTML.trim() === "DELETE") {
      if (confirm("Are you sure you want to delete this task?")) {
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        const EditForm = document.querySelector("#edit-form");
        const formData = new FormData(EditForm);
        fetch(`/delete_task/${btn.getAttribute("task_id")}/`, {
          method: "DELETE",
          body: formData,
          headers: {
              'X-CSRFToken': csrfToken 
          }
        })
        .then((response) => {
          document.getElementById("myEditModal").close();
          location.reload();
          // You can handle the response here (e.g., refresh the page)
        });
      }
    } else {
      btn.innerHTML = "DELETE";
    }
  });
});

ColseModel.addEventListener("click", () => {
  const TaskTranslateField = document.querySelector(".translated-field");
  TaskTranslateField.setAttribute("readonly", "readonly");
  TaskTranslateField.value = " ";
});


DownloadBtn.addEventListener('click', ()=>{
  console.log('object')
  fetch('/download/text/')
  .then(response => response.json)
  .then( data => {
    console.log(data)
  })
})