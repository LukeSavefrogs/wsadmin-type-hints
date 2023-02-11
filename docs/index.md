# Introduction
This project aims to provide a **better developer experience** while developing `wsadmin` scripts for IBM® Websphere Application Server.

It does so by providing:

- **Autocompletion** through the intellisense.
- **Type hints** (function parameters and function return types)


This leads to lots of advantages to the developer, such as:

- **Faster development**, since you don't need to leave the editor to know what was the name of some method.
- **Less errors**, since you don't need to manually re-type the method names and an error will show up if you mistype the methods.

!!! warning

	The `wsadmin` scripting tool only supports **Jython up to 2.7** (some still have Jython 2.1!), so the following requirements must still be satisfied:

	- you MUST use **Python 2 syntax** (check the _Jython_ version to know which one you'll need to target)
	- some packages available on development environments might not be available or might have some differences.

	Make sure to check that your script matches your workplace/environment requirements before submitting it.
	This package DOES NOT in any way prevent you from writing bugged code, or could even contain **old modules** not used anymore in the official documentation (since it was originally written for my workplace production environment using _Websphere Application Server 8.5.5/9.0_ and _Jython 2.1_).

	**Always check that your environment requirements/versions are the same as this library**. 

## Gallery
Here's some screenshots showing the features of this package. The IDE I'm using here is [Visual Studio Code](https://code.visualstudio.com/).

<figure markdown>
  ![Image title](images/60817fad50b7491f2d03e29e93568bfb74dd0ce265319675f2fb83cad67a46fa.png){ width="600" }
  <figcaption>Autocompletion for the <code>AdminControl</code> command.</figcaption>
</figure>

<figure markdown>
  ![Image title](images/e84d4763b6a93d5950af4b85e9b43d04f8fda9b35a9c4d16ed0f52084dd27195.png){ width="600" }
  <figcaption>Type hint for function parameters as well as return types.</figcaption>
</figure>

<figure markdown>
  ![Image title](images/effc6528764e161a1dcd38fd64001001d6b528531ea5638f7e4232075f990949.png){ width="600" }
  <figcaption>An error will show up if you mistype the method.</figcaption>
</figure>

<figure markdown>
  ![Image title](images/81b0b5b198a29fd8c37c63ef095f8ce3972b9d4526dc5e836e94a5b19cb9757e.png){ width="600" }
  <figcaption>Autocompletion based on the <code>AdminConfig.attributes(...)</code> return type (<code>str</code>).</figcaption>
</figure>


## Disclaimer
This is an unofficial package created for speeding up the development process and is not in any way affiliated with IBM®. All trademarks and registered trademarks are the property of their respective company owners.

The code does not include any implementation detail, and includes only the informations (such as parameter numbers, types and descriptions) publicly available on the official Websphere Application Server® documentation.