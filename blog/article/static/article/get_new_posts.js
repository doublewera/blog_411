/**
 * Запомнить момент последнего обращения к БД - с сервера
 * Раз в 5 секунд обращаться на сервер и получать новые посты
 * Встраивать новые посты вверху страницы
 */

//parent.prepend(newChild)

function fetch_new_posts() {
    fetch('last_posts/?dt=2025-06-10+21:45'

    ).then((response) => {
        if (response.status == 200) {
            console.log('Ща всё будет...')
            return response.json()
        }
    }).then((data) => {  // {'posts': [{'user': 'u1', 'text': 't1', 'title': 'smth', 'dt': 'some dt'}]}
        console.log(data)
        let h1;
        for (let p of data.posts) {
            h1 = document.createElement('h1')
            h1.style.color='green'
            h1.textContent = p.dt + ': ' + p.user + ' создал ' + p.title
            document.body.appendChild(h1)
        }
    })
}

window.addEventListener(
    'load',
    () => {
        setInterval(
            fetch_new_posts,  // Функция - без скобочек! Мы её не вызвыаем! Её вызовет браузер, когда придет время
            5000)           // Время в милисекундах между вызовами функции
    }
)

