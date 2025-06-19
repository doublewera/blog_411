function getquestions() {
    console.log('Работает!')
    let url_addr = '/myfetch/?count=6&maxval=10';
    my_promise = fetch(url_addr)
    my_promise.then( 
        // СЮДА надо передать ФУНКЦИЮ, которая ПОЛУЧИТ ОТВЕТ
        (response) => {
            console.log(
                'Ура! Сервер ответил на ', url_addr,
                response.status,
                response)
            // надо проверять код ответа! 200 ок
            // 404 не найден
            // 503 ошибка сервера и т.д.
            return response.json()
        }
    ).then(
        (data) => {
            console.log(data)
            // console.log(q_place.innerHTML)
            // q_place.innerHTML += data
            add_questions(data)
        }
    )
}

function add_questions(data) {
    console.log(data.questions)
    let i = 0;
    for (let pair of data.questions) {
        console.log('Cледующий пример будет ', pair)
        console.log('Следующий пример будет', pair[0], '+', pair[1], '=')
        // следующий пример будет 5+8=?
        // <p>5+8=<input></p>
        // 1. Создать абзац
        let li = document.createElement('li')  // Создать любой элемент
        // 2. Разместить там пример
        li.textContent = pair[0] + '+' + pair[1] + '=';
        q_place.appendChild(li)
        // 3. Создать поле ввода
        let inp = document.createElement('input')
        //inp.value = pair[0] + pair[1]
        inp.setAttribute('name', 'i=' + i + 'q=' + pair[0] + '+' + pair[1])
        // 4. Разместить поле ввода в абзаце
        li.appendChild(inp)
        i++;
    }
}

function checkanswers() {
    let post_me = {}
    for (let key of math_questions) {
        console.log(key)
        if (key.name[0] == 'i') {
            post_me[key.name] = key.value
        }
    }
    console.log(post_me)
    fetch('/check_math/', {
        method: 'POST',
        body: JSON.stringify(post_me),
        //POST: JSON.stringify(post_me),
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        }
    }).then(
        (response) => {
            console.log(
                'Ваш экзамен проверен ',
                response.status,
                response)
            // надо проверять код ответа!
            return response.json()
        }
    ).then(
        (data) => {
            console.log('МЫ СМОГЛИ ПРОЧЕСТЬ ОТВЕТ СЕРВЕРА: ', data)
            // console.log(q_place.innerHTML)
            // q_place.innerHTML += data
            for (let input_name in data) {
                if (data[input_name]) {  // == True
                    math_questions[input_name].setAttribute('class', 'correct')
                } else {
                    math_questions[input_name].setAttribute('class', 'wrong')
                }
            }
        }
    )
}