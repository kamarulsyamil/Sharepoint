from azuretry import SharePoint

#i.e - file_dir_path = r'C:\project\report.pdf'
file_dir_path = r'C:\Users\Kamarul_Syamil\Desktop\Dell\Project\Test4.csv'

# this will be the file name that it will be saved in SharePoint as 
file_name = 'Test4.csv'

# The folder in SharePoint that it will be saved under
folder_name = 'Consolidate View'

# upload file
SharePoint().upload_file(file_dir_path, file_name, folder_name)

# delete file
#SharePoint().delete_file(file_name, folder_name)