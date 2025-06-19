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
        // ОШИБКА! МОГУТ БЫТЬ ПОВТОРЯЮЩИЕСЯ ИМЕНА! НАДО ВСПОМИНАТЬ, СКОЛЬКО У СПИСКА БЫЛО ДЕТЕЙ
        // 4. Разместить поле ввода в абзаце
        li.appendChild(inp)
        i++;
    }
}

function checkanswers() {
    /**
     * Данная функция вызываетс для проверки ответов пользователя на арифметические примеры
     * не потому что JavaScript не мог бы это сделать сам без питона, а чтобы показать,
     * как отправлять данные НА сервер и получить с сервера ОТВЕТ.
     */
    let post_me = {}  // Этот словарь мы отправим на сервер для проверки
    for (let next_input of math_questions) {
        /** Перебираем форму. JavaScript возвращает нам сразу ссылки на поля ввода */
        console.log(next_input)  // Выводить поле ввода в консоль необязательно, но наглядно
        if (next_input.name[0] == 'i') {
            // Если имя поля ввода начинается на i, оно нам подходит. ЭТО НЕ ВСЕГДА ТАК!
            // В нашей задаче поля с вводом от пользователя называются типа 'i=7q=5+5'
            post_me[next_input.name] = next_input.value
            // Записали в словарь, который мы будем отправлять на сервер, новую пару: имя, ответ
        }
    }
    console.log('Отправляем ваши ответы на проверку: ', post_me)  // полюбовались на список ответов пользователя, напечатав его в консоль
    fetch('/check_math/', {
        method: 'POST',
        body: JSON.stringify(post_me),   // Для сервера превратили ответы (объект, словарь, джсон) В СТРОКУ!
        //POST: JSON.stringify(post_me),
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            // БЕЗ ЭТОГО ЗАГОЛОВКА ДЖАНГО НЕ ПРИМЕТ ПОСТ-ЗАПРОС!
        }
    }).then(
        (response) => {
            // ПРИШЛО Обещание от сервера выдать ответ
            console.log(
                'Ваш экзамен проверен ',
                response.status,
                response)
            // надо проверять код ответа! Если 200, то всё ок...
            return response.json()  // Требуем выдать ответ в виде json, ЗНАЯ, что от сервера он пришёл в этом виде
        }
    ).then(
        (data) => {
            console.log('МЫ СМОГЛИ ПРОЧЕСТЬ ОТВЕТ СЕРВЕРА: ', data)
            /**
             * data = {
                    'i=0q=5+10': True,
                    'i=1q=3+3':  True,
                    'i=2q=2+2':  False,
                }
             */
            // От сервера пришли true, false на каждое поле ввода. Их надо пометить классами correct, wrong
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