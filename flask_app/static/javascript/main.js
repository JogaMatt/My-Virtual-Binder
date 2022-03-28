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
        url: "https://api.pokemontcg.io/v2/cards?q=name:" + pokemon
    }).then(function(response){
        console.log(response);
        for (var i = 0; i < response.data.length; i++){
            var pokemonCard = $("<img class='pkmn-card' onmouseover='addShadow(this)' onmouseleave='removeShadow(this)'>");
            pokemonCard.attr("src", response.data[i].images.large);
            $("#card-container").append(pokemonCard);
        }
    });
});