//fetch the items from the json file 
function loadItems(){
    return fetch('data/data.json')
    .then(response => response.json())
    .then(json => json.items);

}
// update the list with the gien items 
function displayItems(items) {
    const container = document.querySelector('.items');
    container.innerHTML = items.map(item => createHTMLString(item)).join("");
}
//create html list items from the given data 
function createHTMLString(item) {
    return `
    <li class="item">
        <img src="${item.image}" alt="${item.type}" class="item_thumbnail" />
        <span class="item_description">${item.gender}, ${item.size}</span>
    </li>
    `;
}
function onButtonClick(event,items) {
    const dataset =event.target.dataset;
    const key = dataset.key;
    const value = dataset.value;
    if (key==null || value==null){
        return;
    }
    displayItems(items.filter(item=>item[key]===value));
}
// Make the items matching {keys:value} invisible.
function updateItems(items,key,value){
    items.forEach(item=>{
        if (item.dataset[key]==value){
            item.classList.remove('invisible');
        }
        else{
            item.classList.add('invisible');
        }
    });
}

function setEventListeners(items){
    const logo = document.querySelector('.logo');
    const buttons = document.querySelector('.buttons');
    logo.addEventListener('click',event=> onButtonClick(event,items));
}
//ㅡmain
loadItems()
.then(items => {
    displayItems(items);
    setEventListeners(items);
})
.catch(console.log);