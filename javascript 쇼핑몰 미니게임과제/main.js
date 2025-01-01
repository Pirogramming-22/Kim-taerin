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
//ㅡmain
loadItems()
.then(items => {

    displayItems(items);
    // setEventListeners(items);
})
.catch(console.log);