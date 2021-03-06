def process_new(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id = order_id)

    if request.method == 'POST':
        # retrieve nonce
        nonce = request.POST.get('payment_method_nonce', None)
        # create and submit transaction
        result = braintree.Transaction.sale({
            'amount': '{:.2f}'.format(order.get_total_cost()),
            'payment_method_nonce': nonce,
            'options': {
                'submit_for_settlement': True
            }
        })
        if result.is_success:
            # mark the order as paid
            order.paid = True
            # store the unique transaction id
            order.braintree_id = result.transaction.id
            order.save()
            return redirect('orders:done')
        else:
            return redirect('orders:cancelled')
    else:
        # generate token
        client_token = braintree.ClientToken.generate()
        return render(
            request,
            'secure/process_new.html',
            {'order':order,
            'client_token':client_token
            }
        )
