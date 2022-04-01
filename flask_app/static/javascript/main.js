function addShadow(element){
    element.classList.add("shadow");
}

function removeShadow(element){
    element.classList.remove("shadow");
}

function increaseSize(element){
    element.classList.add("bigImg")
}

function decreaseSize(element){
    element.classList.remove("bigImg")
}

$("#search-button").on("click", function (event){
    $("#card-container").empty();
    event.preventDefault();
    var pokemon = $("#search_bar")
    .val();
    console.log(pokemon)

    $.ajax({
        method:"GET",
        url: "https://api.pokemontcg.io/v2/cards?q=name:" + pokemon.replace(" ", "*")
    }).then(function(response){
        console.log(response);
        for (var i = 0; i < response.data.length; i++){
            var link = $("<a>");
            link.attr("href", "/card/" + response.data[i].id);
            link.attr("class", "anchor")
            var pokemonCard = $("<img class='pkmn-card' onmouseover='increaseSize(this)' onmouseleave='decreaseSize(this)'>");
            pokemonCard.attr("src", response.data[i].images.large);
            cardLink = link.append(pokemonCard)
            $("#card-container").append(cardLink);
        }
    });
});