$(document).ready(function () {
  //Materialize Initialization
  $('.sidenav').sidenav();
  $('select').formSelect();
  $('textarea#message').characterCounter();
  $('.modal').modal();

  // Code from Code Institute Task Manager
  validateMaterializeSelect();

  function validateMaterializeSelect() {
    let classValid = {
      "border-bottom": "1px solid #4caf50",
      "box-shadow": "0 1px 0 0 #4caf50"
    };
    let classInvalid = {
      "border-bottom": "1px solid #f44336",
      "box-shadow": "0 1px 0 0 #f44336"
    };
    if ($("select.validate").prop("required")) {
      $("select.validate").css({
        "display": "block",
        "height": "0",
        "padding": "0",
        "width": "0",
        "position": "absolute"
      });
    }
    $(".select-wrapper input.select-dropdown").on("focusin", function () {
      $(this).parent(".select-wrapper").on("change", function () {
        if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () {})) {
          $(this).children("input").css(classValid);
        }
      });
    }).on("click", function () {
      if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
        $(this).parent(".select-wrapper").children("input").css(classValid);
      } else {
        $(".select-wrapper input.select-dropdown").on("focusout", function () {
          if ($(this).parent(".select-wrapper").children("select").prop("required")) {
            if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
              $(this).parent(".select-wrapper").children("input").css(classInvalid);
            }
          }
        });
      }
    });
  }
});

// Code modified from Wanderlust Recipes, find more on README
// Add Ingredient
$('#ingredients .add-ingredient-list-item').click(function (event) {
  let IngredientItem = `<li class="collection-item">
                              <div class="input-field">
                                  <input name="ingredients" type="text" class="validate" title="1-100 characters" pattern="^(?=.*[a-zA-Z0-9_ ]){1,100})$" required>
                                  <label for="ingredients">Add quantity and ingredient</label>
                              </div>
                              <a class="remove-list-item">
                                  <i class="fas fa-times"></i>
                                  <span class="sr-only">Remove ingredient</span>
                              </a>
                          </li>`;
  $(this).parent().before(IngredientItem);
});

// Remove Ingredient
$('#ingredients').on("click", ".remove-list-item", function (event) {
  $(this).parent().remove();
});

// Add Method 
$('#method_step .add-method-step-item').click(function (event) {
  let methodStep = `<li class="collection-item">
                          <div class="input-field">
                          <textarea name="method_step" class="materialize-textarea" pattern="^(?=.*[a-zA-Z0-9_ ]){1,100})$" required></textarea>
                          <label for="method_step">Step description</label>
                          </div>
                          <a class="remove-list-item">
                          <i class="fas fa-times"></i>
                          <span class="sr-only">Remove method step</span>
                      </a>
                      </li>`;
  $(this).parent().before(methodStep);
});

// Remove Method 
$('#method_step').on("click", ".remove-list-item", function (event) {
  $(this).parent().remove();
});