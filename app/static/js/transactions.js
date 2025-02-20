requestAnimationFrame(() => {
    if(window.location.pathname == '/transactions/') {
        fetch("/transactions/loadTransactions")
        .then(response => response.json())
        .then(data => {
               console.log(data.data)
                for (let i of data.data){
                    document.querySelector("#content-transactions").appendChild(createTransactionItem(i));
                }
                    
            });
            }
})

function createTransactionItem(item) {
    const contentItem = document.createElement('div');
    contentItem.id = 'content-item-transactions';
    
    // Name item
    const nameItem = document.createElement('div');
    nameItem.className = 'name-item';
    
    const contentName = document.createElement('div');
    contentName.className = 'content-name';
    
    const itemName = document.createElement('span');
    itemName.id = 'name-item';
    itemName.textContent = item.item_name;
    
    contentName.appendChild(itemName);
    nameItem.appendChild(contentName);
    
    // Type item
    const typeItem = document.createElement('div');
    typeItem.className = 'type-item';
    
    const type = document.createElement('span');
    type.id = 'type';
    type.textContent = item.categoria;
    
    typeItem.appendChild(type);
    
    // Amount item
    const amountItem = document.createElement('div');
    amountItem.className = 'amount-item';
    
    const amount = document.createElement('span');
    amount.id = 'amount';
    amount.textContent =  "$ " + item.valor ;
    
    amountItem.appendChild(amount);
    
    // Date item
    const dateItem = document.createElement('div');
    dateItem.className = 'date-item';
    
    const date = document.createElement('span');
    date.id = 'date';
    date.textContent = item.saida_data;
    
    // const hour = document.createElement('span');
    // hour.id = 'hour';
    // hour.textContent = 'at 8:00PM';
    
    dateItem.appendChild(date);
    // dateItem.appendChild(hour);
    
    // Action item
    const actionItem = document.createElement('div');
    actionItem.className = 'action-item';
    
    const viewButton = document.createElement('button');
    viewButton.id = 'view-btn';
    viewButton.textContent = 'View';
    
    actionItem.appendChild(viewButton);
    
    // Status item
    const statusItem = document.createElement('div');
    statusItem.className = 'status-item';
    
    const status = document.createElement('span');
    status.id = 'status';

    if (item.estado == 'Pago') {
        status.style.backgroundColor = "#D9FFE9"
        status.style.color = "var(--green)"
    }
    if (item.estado == "Atrasado"){
        status.style.backgroundColor = "#FFEFEF"
        status.style.color = "var(--error)"
    }

    status.textContent = item.estado;
    
    statusItem.appendChild(status);
    
    // Append all to contentItem
    contentItem.appendChild(nameItem);
    contentItem.appendChild(typeItem);
    contentItem.appendChild(amountItem);
    contentItem.appendChild(dateItem);
    contentItem.appendChild(actionItem);
    contentItem.appendChild(statusItem);
    
    return contentItem;
}

