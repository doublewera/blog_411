// http://127.0.0.1:8000 - нужно редко, только когда идем на другой сайт
//const url_add = '/article/table/'; // ТЕПЕРЬ БЕРЕМ ИЗ form.action

function get_multi_data() {    
    //let num = document.querySelector('input[type=number]').valueAsNumber
    //document.querySelector('input[type=number]').value = ''
    const url_add = document.querySelector('form').action;  // Получили адрес из того хорошего места, где ему положено находиться
    console.log(url_add)

    fetch(url_add + '?zdesbylvasya=3').then(
        (response)=>{
            console.log(response)
            console.log(response.headers);
            // createTable(num)              
            // return response.text()
            return response.json()
        }
    ).then((data) => {
        console.log('А ВОТ И ДАННЫЕ! ', data)
        createTable(data.my_size) 
    })
}

function createTable(num){
    oldtable = document.querySelector('.oldtable')
    if (oldtable){
        oldtable.remove()
    }
    
    table = document.createElement('table')
    table.setAttribute('class', 'oldtable')

    for (let i = 1; i <= num; i++) {
        tr = document.createElement('tr')
        for (let j = 1; j <= num; j++) {
            td = document.createElement('td')
            td.textContent = i * j
            tr.appendChild(td)
        }
        table.appendChild(tr)
             
    }

    document.body.appendChild(table)

}