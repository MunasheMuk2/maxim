document.addEventListener("DOMContentLoaded", async () => {
  const stripe = Stripe(stripePublishableKey);

  const elements = stripe.elements();
  const card = elements.create("card");
  card.mount("#card-element");

  const form = document.getElementById("payment-form");
  const clientSecret = form.dataset.secret;
  const plan = form.dataset.plan;

  form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const { error, paymentIntent } = await stripe.confirmCardPayment(clientSecret, {
      payment_method: {
        card: card,
        billing_details: {
          name: document.getElementById("name").value,
        },
      },
    });

    if (error) {
      document.getElementById("card-errors").textContent = error.message;
    } else {
      window.location.href = `/checkout/success/?plan=${plan}`;
    }
  });
});