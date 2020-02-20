import javax.xml.bind.DatatypeConverter;
import java.io.File;
import java.io.FilenameFilter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class Main {
    public static void main(String[] args) throws IOException, NoSuchAlgorithmException {
        String testInputPath = "/home/wan/Desktop/ShawnJin_Workspace/Tools/DuplicateFileChecker/duplicate_test_folder";
        Path testPath = Paths.get(testInputPath);
        System.out.println("Checking duplicate files...");
        File[] files = getFiles(testPath);
        System.out.println("Size: " + files.length);

        Path currentPath = testPath;
        for (File file : files) {
//            currentPath.
            System.out.println(file.getName() + ": " + getMD5CheckSum(file.toPath()));
        }
        System.out.println("--------------------");
        File[] folders = getFolders(testPath);
        for (File folder: folders) {
            System.out.println(folder.getName());
        }
    }

    /**
     * calculate the md5 checksum of a file
     * @param path the path to the file
     * @return a string of md5 encode
     * @throws NoSuchAlgorithmException
     * @throws IOException
     */
    private static String getMD5CheckSum(Path path) throws NoSuchAlgorithmException, IOException {
        MessageDigest messageDigest = MessageDigest.getInstance("MD5");
        messageDigest.update(Files.readAllBytes(path));
        return DatatypeConverter.printHexBinary(messageDigest.digest()).toUpperCase();
    }


    private static File[] getFolders(Path path) {
        File directory = new File(String.valueOf(path));
        FilenameFilter isDirectory = (file, s) -> file.isDirectory();
        File[] files = directory.listFiles(isDirectory);



        return files;
    }

    private static File[] getFiles(Path path) {
        File directory = new File(String.valueOf(path));
        FilenameFilter isFile = (file, s) -> !file.isDirectory();
        File[] files = directory.listFiles(isFile);



        return files;
    }
}
