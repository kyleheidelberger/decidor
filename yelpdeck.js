
// fetches data from iTunes API and returns it (using variable 'searchText')
function searchYelp(zipCode) {
    return fetch(`https://cors-anywhere.herokuapp.com/https://api.yelp.com/v3/businesses/search?categories=food,all&location.zip_code=${zipCode}`, {
        headers: {
            "Access-Control-Allow-Origin": "*",
            "Authorization": `Bearer SM6pJx7LlCeKgElTpKU3PgsBDvqZud92PBBhqRBOEunqL9az6MmnAN9GUf4_mjjQva10STsyAlOs6RacEdskjV3qx7X_SjhqtpFVY0G0KzKvDoXcb4s-X2eZHOc5XXYx`
        }
    }
    )
        .then(function (response) {
            if (!response.ok) {
                throw Error(response.statusText)
            }
            return response.json()

        })
}


// display results of search
function showResults(zipCode) {
    // call searchYelp to get API data
    searchYelp(zipCode)
        .then(function (data) {
            console.log(data)

            // grabs result list div and sets it to empty
            const resultList = document.querySelector('#result-list')
            resultList.innerHTML = ''

            // loops through data.businesses array
            for (index = 0; index < data.businesses.length; index++) {

                // create a div for each result
                const result = document.createElement('div')
                //then creates separate div elements inside result div for info and cover img
                const resultInfo = document.createElement('div')
                const resultImage = document.createElement('div')

                // add classes to divs
                result.classList.add('result')
                resultInfo.classList.add('result-details', 'container')
                resultImage.classList.add('result-image-div', 'container')

                // assigns data from fetch businesses to variables:
                let resultName = data.businesses[index].name
                let resultImageURL = data.businesses[index].image_url


                // puts data into divs
                resultInfo.innerHTML = `<ul class="unstyled"><li><strong>${resultName}</strong></li></ul>`
                resultImage.innerHTML = `<img class="resultArt" src="${resultImageURL}">`

                // update the new result
                result.append(resultImage, resultInfo)
                // update result list with new result
                resultList.append(result)

            }

        })
}



// Main Execution

document.addEventListener('DOMContentLoaded', function () {
    // assigns search bar to variable userSearch
    let button = document.querySelector('.button')
    // adds 'change' event to userSearch so that event occurs when input is changed
    // event.preventDefault prevents page from refreshing
    button.addEventListener('click', function (event) {
        event.preventDefault()
        // adds user term= to user input and encodes for url
        let zipCode = encodeURIComponent(button.value)
        console.log(zipCode)
        // clears the search
        button.value = ''

        // calls the search function
        showResults(zipCode)
    })
})