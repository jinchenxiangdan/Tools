import javax.xml.bind.DatatypeConverter;
import java.io.File;
import java.io.FilenameFilter;
import java.io.IOException;
import java.nio.file.FileAlreadyExistsException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.HashMap;
import java.util.Map;

public class Main {
    private static HashMap<String, String> CHECKSUM_HASHMAP = new HashMap<>();
    private static final String duplicate_content_files_name   = "duplicate_content_files";
    private static final String duplicate_name_files_name      = "duplicate_name_files";
    private static final String duplicate_all_files_name       = "duplicate_all_files";
    private static Path DUPLICATE_CONTENT_FOLDER;
    private static Path DUPLICATE_NAME_FOLDER;
    private static Path DUPLICATE_ALL_FOLDER;
    private static Path CURRENT_PATH;

    public static void main(String[] args) throws IOException, NoSuchAlgorithmException {


        // for testing
        String testInputPath = "/home/wan/Desktop/ShawnJin_Workspace/Tools/DuplicateFileChecker/duplicate_test_folder";
        CURRENT_PATH = Paths.get(testInputPath);
        Path duplicateFolderPath = CURRENT_PATH.subpath(0, CURRENT_PATH.getNameCount()-1);
//        System.out.println("Path is : " + duplicateFolderPath);
        //
        System.out.println("Checking duplicate files...");
        // create directories to store invalid files
        try {
            DUPLICATE_ALL_FOLDER = Files.createDirectory(Paths.get("/", duplicateFolderPath.toString(), duplicate_all_files_name));
        } catch (FileAlreadyExistsException e) {
            DUPLICATE_ALL_FOLDER = Paths.get("/", duplicateFolderPath.toString(), duplicate_all_files_name);
            System.out.println("Directory already exists, pass through...");
        } catch (IOException e) {
            e.printStackTrace();
        }

        try {
            DUPLICATE_CONTENT_FOLDER = Files.createDirectory(Paths.get("/", duplicateFolderPath.toString(), duplicate_content_files_name));
        } catch (FileAlreadyExistsException e) {
            DUPLICATE_CONTENT_FOLDER = Paths.get("/", duplicateFolderPath.toString(), duplicate_content_files_name);
            System.out.println("Directory already exists, pass through...");
        } catch (IOException e) {
            e.printStackTrace();
        }

        try {
            DUPLICATE_NAME_FOLDER = Files.createDirectory(Paths.get("/", duplicateFolderPath.toString(), duplicate_name_files_name));
        } catch (FileAlreadyExistsException e) {
            DUPLICATE_NAME_FOLDER = Paths.get("/", duplicateFolderPath.toString(), duplicate_name_files_name);
            System.out.println("Directory already exists, pass through...");
        } catch (IOException e) {
            e.printStackTrace();
        }

        // get current folders
        File[] folders = getFiles(CURRENT_PATH);
        // loop directory 
        for (File folder : folders) {
            if (folder.isDirectory()) {
                // move to this directory
                System.out.printf("Moving to directory %s \n", folder.getName());
                checkDuplicate(folder.toPath());
                System.out.println("Done.");
            } else {
                System.out.printf("Alert: a file %s exist under %s\n", folder.getName(), CURRENT_PATH.toString());
            }
        }
//        for (File file : folders) {
//            if (file.isFile())  System.out.println(file.getName() + ": " + getMD5CheckSum(file.toPath()));
//        }
        System.out.println("------testing-------");
        printHashMap();

    }

    /**
     * calculate the md5 checksum of a file
     * @param path the path to the file
     * @return a string of md5 encode
     * @throws NoSuchAlgorithmException
     * @throws IOException
     */
    private static String getMD5CheckSum(Path path) throws NoSuchAlgorithmException, IOException {
        if (Files.isDirectory(path)) {
            System.out.printf("Path %s is a directory, cannot use checksum\n", path);
            return null;
        }
        MessageDigest messageDigest = MessageDigest.getInstance("MD5");
        messageDigest.update(Files.readAllBytes(path));
        return DatatypeConverter.printHexBinary(messageDigest.digest()).toUpperCase();
    }


    /**
     * list all files under that path
     * @param path the path you want to list files
     * @return a list of files
     */
    private static File[] getFiles(Path path) {
        File directory = new File(String.valueOf(path));
//        FilenameFilter isFile = (file, s) -> !file.isDirectory();
        return directory.listFiles();
    }


    /**
     * check duplication of files under input path
     * Precondition: Under that directory. only has files
     * @param path the path you want to check
     * @throws IOException
     * @throws NoSuchAlgorithmException
     */
    private static void checkDuplicate(Path path) throws IOException, NoSuchAlgorithmException {
        File[] files = getFiles(path);
        if (files == null) {
            System.out.printf("Path : %s is not a directory.\n", path);
            return;
        }
        boolean hasChecksum, hasFileName;
        for (File file : files) {
            String checksum = getMD5CheckSum(file.toPath());
            if (checksum == null) {
                continue;
            }
            String fileName = file.getName();
            if (CHECKSUM_HASHMAP.containsKey(checksum)) {
                hasChecksum = true;
            } else {
                hasChecksum = false;
            }
            
            if (CHECKSUM_HASHMAP.containsValue(fileName)) {
                hasFileName = true;
            } else {
                hasFileName = false;
            }
            
            
            
            if (!hasChecksum && !hasFileName) {
                CHECKSUM_HASHMAP.put(checksum, fileName);
                System.out.println("added to hash map");
                // add to hashtable 
            } else if (!hasChecksum) {
                // move to folder <>
                System.out.printf("Moving file %s to folder %s with path %s\n", file.getName(), DUPLICATE_CONTENT_FOLDER.toString(),
                        file.toPath().subpath(CURRENT_PATH.getNameCount(), file.toPath().getNameCount()-1));
            } else if (!hasFileName) {
                // move to folder <>
                System.out.printf("Moving file %s to folder %s with path %s\n", file.getName(), DUPLICATE_NAME_FOLDER.toString(),
                        file.toPath().subpath(CURRENT_PATH.getNameCount(), file.toPath().getNameCount()-1));
            } else {
                // move to folder<>
                System.out.printf("Moving file %s to folder %s with path %s\n", file.getName(), DUPLICATE_ALL_FOLDER.toString(),
                        file.toPath().subpath(CURRENT_PATH.getNameCount(), file.toPath().getNameCount()-1));
            }
            
        }
    }

    /**
     * Print out the hash map, this is for debugging
     */
    private static void printHashMap() {
        for (Map.Entry<String, String> entry : CHECKSUM_HASHMAP.entrySet()) {
            System.out.println(entry.getKey() + " -- " + entry.getValue());
        }
    }
}
