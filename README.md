#DocSearch

## Dependencies
### For Demo/Testing
If you want to purely run this for testing purposes, you will only need `docker`.

See the below table for installing Docker Desktop for your OS:
|   OS    | Link                                                     |
| :-----: | :------------------------------------------------------- |
| Windows | https://docs.docker.com/desktop/install/windows-install/ |
|   Mac   | https://docs.docker.com/desktop/install/mac-install/     |
|  Linux  | https://docs.docker.com/desktop/install/linux-install/   |

### For Development
TODO: Add doc info here

## How to Run
### Using Docker
If you are running this for demo purposes, first run the following command:

```docker build -t doc-search:<tag-version> https://github.com/Daepak98/DocSearch.git```

Make sure to replace `<tag-version>` with the current version, which for now is `0.0.1`. This command will create the Docker image that will form the basis for the container.

Then run the following command:

```docker run -d -p 5000:5000 doc-search:<tag-version>```

Again, make sure to use the `<tag-version>` specified in the `docker build` command. This command will create and run a container with the `doc-search` image as a base. If the container spins up correctly, the command will output a container ID, as well as you should be able to view the container in Docker Desktop. 

With the application up and running, you can navigate to your browser and go to `http://localhost:5000/` and you should be able to see a page that just says "Home?". This is because the website is still a WIP. However, if you add documents to the container's `docs` folder, you can append the document's name (without the extension) to the end of the URL and get a document in return. As a test, you can do this with the dummy PDF that is already in the `docs` folder, `output.pdf`. If is intentionally empty, but it should suffice to show that when you go to `http://localhost:5000/output`, you will get the `output.pdf` document back.

### During Development
TODO: Add doc info here too