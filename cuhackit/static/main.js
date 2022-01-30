var tid = setInterval(getCards, 1000);

var cards = new Set();

function getCards(){
  $.ajax({
    type: "GET",
    url: "/posts",
  }).done((data) => {
    for (e of data){
      addCard(e);
    }
  })
}

function addCard(card)
{
  if (!('postID' in card) || cards.has(card['postID'])){
    return;
  }
  cards.add(card['postID']);
  val = card['value'];
  card_html = `
  <div class="card" style="width: 18rem; height: 18rem; margin: 15px">
    <div class="card-body">
      <h5 class="card-title">${card["title"]}</h5>`
      if (val.startsWith("http")){
        card_html += `<img src="${card["value"]}">`;
      } else {
        card_html += `<p class="card-text">${card["value"]}</p>`;
      }
      + `
      
    </div>
  </div>`
  cards_div = document.getElementById("cards-div");
  cards_list = document.getElementById("cards-list");
  li = document.createElement('li');
  li.innerHTML = card_html;
  // cards_list.appendChild(li);
  cards_list.insertBefore(li, cards_list.firstChild);
}
function submitPost(){
    title_box = document.getElementById("title-box");
    value_box = document.getElementById("value-box");
    $.ajax({
        type: "POST",
        url: "/post",
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        data: JSON.stringify({
          "title": title_box.value,
          "value": value_box.value
        })
    }).done((data) => {})
}