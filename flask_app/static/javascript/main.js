function addShadow(element){
    element.classList.add("shadow");
}

function removeShadow(element){
    element.classList.remove("shadow");
}

$("#submit-button").on("click", function (event){
    $("#card-container").empty();
    event.preventDefault();
    var pokemon = $("#search_bar")
    .val()
    .trim();

    $.ajax({
        method:"GET",
        url: "https://api.pokemontcg.io/v1/cards/?name=" + pokemon
    }).then(function(response){
        for (var i = 0; i < response.cards.length; i++){
            var pokemonCard = $("<img class='pkmn-card' onmouseover='addShadow(this)' onmouseleave='removeShadow(this)'>");
            pokemonCard.attr("src", response.cards[i].imageUrlHiRes);
            $("#card-container").append(pokemonCard);
        }
    });
});