[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
<br />
<p align="center">
  <h2 align="center">Skill-DB</h2>

  <p align="center">
    This is a show case repo I created to expose my development skills to prospective customers.
    <br />
    <a href="https://github.com/dafis/skilldb">View Demo</a>
    ·
    <a href="https://github.com/dafis/skilldb/issues">Report Bug</a>
    ·
    <a href="https://github.com/dafis/skilldb/issues">Request Feature</a>
  </p>
</p>


## About The Project

This project is mentioned as a show case for my development skills.
I plan to install it on AWS and use it as an personal online profile. 
As it is an open source projekt, you are free to copy and use it on your own.

### Built With

* [Django](https://www.djangoproject.com/)
* [Wagtail](https://wagtail.io/)

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

This repo is only tested for a linux installations. Python >= 3.6 must be installed.


### Installation

1. Clone the skilldb
   ```sh
   git clone https://github.com/dafis/skilldb.git
   ```

2. create a python environment and activate it
   ```sh
   cd skilldb
   python3 -m venv .venv
   . .venv/bin/activate
   ```

3. install the required python packages
   ```sh
   pip3 install -r requirements.txt
   ```

4. perform the migration steps
   ```sh
   python3 manage.py migrate
   python3 manage.py createsuperuser
   ```

## Usage

1. run the server in dev mode
   ```sh
   python3 manage.py runserver
   ```

## Roadmap

See the [open issues](https://github.com/dafis/skilldb/issues) for a list of proposed features (and known issues).


## Contributing

As I plan to go back to a close source project, it is not recommended to contribute to this project, but you are free
and welcome to fork the project. I would also rethink my plan and stay with open source, if many of you wish so.

If you still want to contribute, here's how. And don't forget to ask me, if I would accept the changes, before you
invest too much time.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT license. See `LICENSE` for more information.

## Contact

Peter Paul Kiefer - [@pkiefer42](https://twitter.com/pkiefer42) - dafisppk@gmail.com

[contributors-shield]: https://img.shields.io/github/contributors/dafis/skilldb.svg?style=for-the-badge
[contributors-url]: https://github.com/dafis/skilldb/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/dafis/skilldb.svg?style=for-the-badge
[forks-url]: https://github.com/dafis/skilldb/network/members
[stars-shield]: https://img.shields.io/github/stars/dafis/skilldb.svg?style=for-the-badge
[stars-url]: https://github.com/dafis/skilldb/stargazers
[issues-shield]: https://img.shields.io/github/issues/dafis/skilldb.svg?style=for-the-badge
[issues-url]: https://github.com/dafis/skilldb/issues
[license-shield]: https://img.shields.io/github/license/dafis/skilldb.svg?style=for-the-badge
[license-url]: https://github.com/dafis/skilldb/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/dafis
