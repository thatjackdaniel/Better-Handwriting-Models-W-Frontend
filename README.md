What can i say about my first high-accurachy language model built from NMIST dadtaset class? well, it sucked and the model the teacher designed only hit 92% accuracy. The front end he designed, as he insisted on making it a mac only design and build environment, does not appeal to all learners on all platforms. I strived to bring you the original model, which i only added batch normalization, aiming for 99%+ val accuracy and simply put, batch normalization did just that! 

The numbers in the file names on the hw models are the highest i pulled in each type. changing epoch lengths can changes your output success// you can try these out for yourself and tweak them. The idea was to show you all the different possible ways to tweak this model to push for super high accuracy in small nukmber of epochs in a way that a normal laptop can train in an hour or hopefully less. I think we have a few beautiful examples and also showcase the new frontend so let's get to that.. 

The frontend i was taught to make can only be created an ran using iOS which is bery shortsighted. I don't care what your favorite OS is or pc brand, Strive to make code that transcends platforms and connects information to people who need it. yes? ok. Instead of soe fancy pants third party software build we simply designed a PyQt5 Conatainer app with a drawing interface. 

If you have tackled this NMIST hadnwriting model before, then you know that the real issue lies in the interface. your model trains out high but the interface, but the interface returns bad guesses because when scaling your drawing of the written integer down to 28,28,1 it becomes a thik blurry blobby mess(i'll try to rememebr to include a screener of the bad digit of a 5 i captured). 

We remedy this in a two-fold manner, through the use of image centering, which look at an image and deetermines  to the best of its abilites which way is right side up and cneters the image before shrinking. this keeps asa much of the written integer in the picture as possible. next we thin down the pixel thickness of the line on the bacside AND in the fron just a little. This gives us a clear integer and before you know it, our model it running flawlessly!! 

in the end, we have a basic single conv block model and also the full-tilt triple conv block with lronplateau, adam optimizer and more to push for insane accuracy
 
 I hope that this helps you if you have had any issues with high-accurcy language models like this one build on NMIST datasets
