const TodoTask = document.querySelectorAll('.todo-task')
const Options = JSON.parse(document.getElementById('radioButtonsContainer').getAttribute('user_lan'));
const TaskInput = document.querySelector('.task-translate')

function createRadioButtons(options) {
    const container = document.getElementById('radioButtonsContainer');
    console.log(container)
    container.innerHTML = " "
    // Loop through the options and create radio buttons
    for (let i = 0; i < options.length; i++) {
        const option = options[i];

        // Create the radio button input element
        const radioInput = document.createElement('input');
        radioInput.type = 'radio';
        radioInput.id = 'option' + i;
        radioInput.name = 'options';
        radioInput.value = option;
        radioInput.style.color = 'black';

        // Create the label for the radio button
        const radioLabel = document.createElement('label');
        radioLabel.htmlFor = 'option' + i;
        radioLabel.textContent = option;
        radioLabel.style.color = 'black';

        // Append the radio button and label to the container
        container.appendChild(radioInput);
        container.appendChild(radioLabel);

        // Add a line break to separate radio buttons
        container.appendChild(document.createElement('br'));
    }
}

TodoTask.forEach(task => {
    task.addEventListener('click', () => {
        console.log(task.innerHTML)
        const ModalCard = document.querySelector('.modal-card')
        ModalCard.innerHTML = task.innerHTML
        TaskInput.setAttribute('value', task.innerHTML.trim())
        createRadioButtons(Options)
    })
});