
/*
List of endpoints:
  GET - http://localhost:8000/hello -> {'Hello': 'World'} Here as an example
  GET - http://localhost:8000/menu -> {'items': menu} A dict of the menu
  POST - http://localhost:8000/latest-order -> A dict of the latest order
  POST - http://localhost:8000/orders -> An endpoint to handle an order. The order is in the http body as so: { 'items': items }

*/

const currentOrder = [];


async function fetchProducts() {
    /**
    this function fetches the products on the menu.
    input: none
    returns: none
     */
    const response = await fetch("http://localhost:8000/menu");

    if (response.ok) {
        return response.json();
    } else {
        throw response.status;
    }
}


async function orderUpdater(form) {
    /**
    this function gets an order form and updates the order array as the order
    input: form of the menu
    returns: None
    */
    //index 0 = event name, 1 = event price, 2 = event quantity, 3=id , 4=description
    currentOrder[form.dataset.data - 1][2] = Number(form.value);
    // sortArray();
    orderStyleUpdater();
}


function orderStyleUpdater() {
    /**
    this function updates the products order to the dom
    input: none
    returns: none
     */
    const orderElement = document.getElementById("myOrder");
    orderElement.innerHTML = "";
    let flag = true;

    for (let i = 0; i < currentOrder.length; i++) {
        if (currentOrder[i][2] != 0) {
            const newElement = document.createElement("p");
            newElement.textContent += `${currentOrder[i][0]} (${currentOrder[i][2]}) X ${currentOrder[i][1]} = $${currentOrder[i][1] * currentOrder[i][2]}`;
            orderElement.appendChild(newElement);
            flag = false;
        }
    }

    if (flag) {
        const newElement = document.createElement("p");
        newElement.textContent += `Empty Order`;
        orderElement.appendChild(newElement);
    }
}


async function appendProducts() {
    /**
    this function adds the menu elements to the dom
    input: none
    returns: none
     */
    try {
        const data = await fetchProducts();
        const gif = document.getElementById("loader");
        gif.style.display = "none";
        const childNodes = [];



        for (product in data.items) {
            currentOrder.push([data.items[product].name, Number(data.items[product].price), 0, Number(data.items[product].id), data.items[product].description]);
            const container = document.getElementById("menu")

            const newForm = document.createElement("input");
            newForm.className = 'form';
            newForm.type = "number";
            newForm.min = "0";
            newForm.max = "5";
            newForm.value = "0";
            newForm.innerHTML = `<input type="number" name="tentacles" min="0" max="5" value="0" />`;
            newForm.dataset.data = currentOrder.length


            const newDiv = document.createElement("div");
            newDiv.style.backgroundColor = "#434242";
            newDiv.style.padding = "1rem";

            const newHeading = document.createElement("h3");
            const newDescription = document.createElement("p");
            newHeading.textContent = `${data.items[product].name} ($${data.items[product].price})`;
            newDescription.textContent = data.items[product].description;

            newDiv.appendChild(newHeading);
            newDiv.appendChild(newDescription);
            newDiv.appendChild(newForm);
            newDiv.dataset.data = data.items[product].price;

            container.appendChild(newDiv);
            childNodes.push(newDiv);
            newForm.addEventListener("change", func = () => orderUpdater(newForm));
        }


        //sort by price
        childNodes.sort(function (a, b) {
            return Number(a.dataset.data) == Number(b.dataset.data)
                ? 0
                : (Number(a.dataset.data) > Number(b.dataset.data) ? -1 : 1);
        });

        for (i = 0; i < childNodes.length; ++i) {
            document.getElementById("menu").appendChild(childNodes[i]);
        }

    } catch (error) {
        console.error(error);
    }
}


async function fetchLatestOrder() {
    /**
     * this function fetches latest order.
     */
    return new Promise((resolve, reject) => {
        fetch("http://localhost:8000/latest-order")
            .then((response) => {
                if (response.ok) {
                    return response.json();
                } else {
                    throw response.status;
                }
            })

            .then((data) => {
                resolve(data);
            })
            .catch((error) => {
                reject(error);
            });
    })
}

async function appendLatestOrder() {
    /**
     * this function appends latest order to the dom
     * input None
     * returns None
     * Seems to be a problem with the server, tried to look in py code but nothing is wrong.
     */
    data = await fetchLatestOrder();
    console.log(data);
    const latestOrder = document.getElementById("latest-order-info")
    latestOrder.innerHTML = "";
    for (product in data.items) {
        if (data.items[product].quantity > 0) {
            const newDiv = document.createElement("div");
            newDiv.style.backgroundColor = "#434242";
            newDiv.style.padding = "1rem"
            const newHeading = document.createElement("h3");
            newHeading.textContent = `${data.items[product].name} ($${data.items[product].price}) X ${data.items[product].quantity}`;
            newDiv.appendChild(newHeading);
            latestOrder.appendChild(newDiv);
        }
    }

}

//main logic:
const submit = document.getElementById("submit-button");
const latestOrderButton = document.getElementById("get-last-order-button");
latestOrderButton.addEventListener("click", appendLatestOrder)
submit.addEventListener("click", func = () => {
    let myOrder = {
        'items': [{ "description": currentOrder[0][4], "id": currentOrder[0][3], "name": currentOrder[0][0], "price": currentOrder[0][1], "quantity": currentOrder[0][2] }, { "description": currentOrder[1][4], "id": currentOrder[1][3], "name": currentOrder[1][0], "price": currentOrder[1][1], "quantity": currentOrder[1][2] }, { "description": currentOrder[2][4], "id": currentOrder[2][3], "name": currentOrder[2][0], "price": currentOrder[2][1], "quantity": currentOrder[2][2] }, { "description": currentOrder[3][4], "id": currentOrder[3][3], "name": currentOrder[3][0], "price": currentOrder[3][1], "quantity": currentOrder[3][2] }]
    };
    fetch('http://localhost:8000/orders', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(myOrder)
    })
        .then(response => {
            console.log(response.status)
            alert("Order successful!")
        })
        .catch(error => {
            console.error(error)
            alert("Failed to process order!")
        })
})

appendProducts()
