from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Wishlist
from .forms import WishlistForm


@login_required
def show_wishlist(request):
    """ A view to show the user's product wishlists """
    user = request.user
    wishlists = Wishlist.objects.filter(user=user)

    template = 'wishlist/wishlist.html'

    context = {
        'wishlists': wishlists,
    }

    return render(request, template, context)


@login_required
def add_wishlist(request, product_id):
    """ Display form to add a wishlist to a product """
    product = get_object_or_404(Product, pk=product_id)
    user = request.user
    user_wishlist = Wishlist.objects.filter(
        user=user, product=product)

    # Check if user already submitted a wishlist for the product
    if user_wishlist:
        messages.error(request,
                       'You have already submitted a wishlist for this product')
        return redirect(reverse('product_detail', args=[product.id]))
    else:
        if request.method == 'POST':
            form = WishlistForm(request.POST, request.FILES)
            if form.is_valid():
                form.instance.user = request.user
                form.instance.product = product
                form.save()
                messages.success(request,
                                 'Your product wishlist has been submitted')

                return redirect(reverse('product_detail', args=[product.id]))
            else:
                messages.error(request, 'Failed to submit the wishlist. \
                    Please ensure the form is valid.')
        else:
            form = WishlistForm()

    template = 'wishlist/add_wishlist.html'

    context = {
        'product': product,
        'form': form,
    }

    return render(request, template, context)


@login_required
def delete_wishlist(request, wishlist_id):
    """ Delete an existing wishlist """
    wishlist = get_object_or_404(Wishlist, pk=wishlist_id)

    if request.user != wishlist.user:
        messages.error(request, 'You are not authorized \
            to delete this wishlist.')
        return redirect(reverse('product_detail', args=[wishlist.product.id]))

    wishlist.delete()
    messages.success(request, 'Your wishlist has been deleted!')
    print('wishlist', wishlist)

    return redirect(reverse('product_detail', args=[wishlist.product.id]))