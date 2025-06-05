console.log('Работает!')
let url_addr = '/';
fetch(url_addr).then( 
    // СЮДА надо передать ФУНКЦИЮ, которая ПОЛУЧИТ ОТВЕТ
    (response) => {
        console.log(
            'Ура! Сервер ответил на ', url_addr,
            response.status,
            response)
        return response.text()
    }
).then(
    (data) => {
        console.log(data)
    }
)