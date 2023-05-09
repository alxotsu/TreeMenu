const menuDiv = document.getElementById("menu");
const template = document.getElementById("menu-item");

let once = true;

function add_item(item){
    let clone = template.content.cloneNode(true);
    clone.getElementById("item-name").textContent = item.name;
    clone.firstElementChild.addEventListener("click", () => {
        if (once){
            once = false;
            window.location.href = `/menu/${menu_name}/${item.name}/`;
        }
    });

    if (item.name === active_item_name){
        console.log(item.name);
        clone.firstElementChild.classList.add("active");
    }
    let childrenContainer = clone.getElementById("children");
    for (child of item.children) {
        childDiv = add_item(child, item);
        childrenContainer.appendChild(childDiv);
    }

    return clone;
}

for (root of menu_structure) {
    menuDiv.appendChild(add_item(root));
}
