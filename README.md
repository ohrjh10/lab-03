# Lab 3
[Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repo and clone it to your machine to get started!

## Team Members
Junhyung(Richard) Oh

## Lab Question Answers
Question 1: Why are RESTful APIs scalable?

There is a separation between the client and the server which makes it easier for the developers to scale.
For example, changes in the server does not affect the client immediately, which gives more flexibility for the developers to edit.

Question 2: According to the definition of “resources” provided in the AWS article above, What are the resources the mail server is providing to clients?

Resources are the information that different applications provide to their clients. Resources can be images, videos, text, numbers, or any type of data.
The mail server is providing resources such as the mail entries, the mail sender, the id of corresponding mails in this lab.

Question 3: What is one common REST Method not used in our mail server? How could we extend our mail server to use this method?

PATCH, which is a common method used to updating resources on the server is not used. We can extend our mail server by using patch so that the mail entry are up to date.

Question 4: Why are API keys used for many RESTful APIs? What purpose do they serve?

API keys are used as a form of authentication. 
Through the use of API keys, we are able to block access from unauthorized connections and therefore it is more secured as only people with access can get information
from the RESTful APIs.

Source: https://cloud.google.com/endpoints/docs/openapi/when-why-api-key#:~:text=API%20keys%20provide%20project%20authorization,-To%20decide%20which&text=By%20identifying%20the%20calling%20project,or%20enabled%20in%20the%20API.

...
