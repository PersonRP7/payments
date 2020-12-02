# Django based braintree payment gateway with SCA/3DS2 enabled

## General:

A minimalistic, no frills approach to 3DS2 implementation. To wit, it differs from the official braintree
example in several respects. The client token (which is a necessity for 3DS2 implementation) is sent to the 
template context by the corresponding view / controller function upon a GET request as opposed to using an XHR
request to braintree's accompanying endpoint. Accessory function have been removed for the sake of brevity.

The javascript is started using the ```onFetchClientToken``` function which instantiates the dropin inside of a 
form div. Within the js, the dropin is sent to the globally declared ```dropin``` variable, which is then passed
to the form's event listener. 
