
#Use this to quickly disable all the debug renderers before submit
ALLOW_DEBUG_RENDERERS = True

RENDER_DEBUG_CHECKOUT_AREA = True and ALLOW_DEBUG_RENDERERS
RENDER_DEBUG_PLAYER_COLLIDERS = True and ALLOW_DEBUG_RENDERERS
RENDER_DEBUG_BUTTON_COLLIDERS = True and ALLOW_DEBUG_RENDERERS

#Config

# How many scores can be shown at once (deletes excess)
SCORES_MAX_LENGTH = 20

# How many items (can be of the same type), the shopping list will have (at max, though levels should have enough spots)
MAX_SHOPPING_LIST_COUNT = 1

# How many items can be kept in a cart
CART_MAX_CAPACITY = 10