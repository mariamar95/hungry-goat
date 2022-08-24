$(document).ready(function(){
  //Materialize Initialization
  $('.sidenav').sidenav();
  $('select').formSelect();
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