//
//  TableViewController.swift
//  MathNews
//
//  Created by cs laptop on 2/16/16.
//  Copyright (c) 2016 cs121MathNewApp. All rights reserved.
//

import UIKit
import Firebase

class TableViewController: UITableViewController {
    //create empty arrays for titles, blurbs, urls
    var titleArray = [String]()
    var blurbArray = [String]()
    var urlArray = [String]()

    override func viewDidAppear(animated: Bool) {
        super.viewDidAppear(animated)
        
        // Create reference to database
        // Currently references articles sub-category
        let ref = Firebase(url:"https://crackling-torch-4312.firebaseio.com/articles")
        
        // Retrieve new articles as they are added to your database
        ref.observeEventType(.ChildAdded, withBlock: { snapshot in
       
        if (snapshot.value.objectForKey("title") != nil)
        {
            let title = snapshot.value.objectForKey("title")!
            self.titleArray.append(title as! String)
        }
        else if (snapshot.value.objectForKey("title") == nil)
        {
            self.titleArray.append(" ")
        }
        if (snapshot.value.objectForKey("blurb") != nil)
        {
            let blurb = snapshot.value.objectForKey("blurb")!
            self.blurbArray.append(blurb as! String)
        }
        else if (snapshot.value.objectForKey("blurb") == nil)
        {
            self.blurbArray.append(" ")
        }
        if (snapshot.value.objectForKey("url") != nil)
        {
            let url = snapshot.value.objectForKey("url")!
            self.urlArray.append(url as! String)
        }
        else if (snapshot.value.objectForKey("url") == nil)
        {
            self.urlArray.append(" ")
        }
        
            
        //reload table with above data
        self.tableView.reloadData()
        
        }, withCancelBlock: { error in
                print(error.description)
                
        })
        
        ref.observeEventType(.ChildRemoved, withBlock: { snapshot in
            self.titleArray = []
            self.blurbArray = []
            self.urlArray = []
            self.tableView.reloadData()
        })
  
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        //Change the color of the navigation controller and text color
        // self.navigationController?.navigationBar.barTintColor = UIColor.lightGrayColor()
        self.navigationController?.navigationBar.titleTextAttributes = [NSForegroundColorAttributeName:UIColor(red: 0.0/255.0, green: 137.0/255.0, blue: 237.0/255.0, alpha: 1.0) ]

        //sets the table's background to white
        self.tableView.backgroundColor = UIColor.whiteColor()
        //gets rid of the unoccupied cells
        tableView.tableFooterView = UIView(frame:CGRectZero)


    }

    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    // MARK: - Table view data source

    override func numberOfSectionsInTableView(tableView: UITableView) -> Int {
        // Return the number of sections.
        return 1
    }

    override func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        // Return the number of rows in the section.
        return titleArray.count
    }

    
    override func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        let cellIdentfier = "ArticleTableViewCell"
        let cell = tableView.dequeueReusableCellWithIdentifier(cellIdentfier, forIndexPath: indexPath) as!ArticleTableViewCell

        //Configure the cell
		//Display title
        cell.LinkLabel?.text = titleArray[indexPath.row]
        
        //Display blurb
        cell.ContentLabel?.text = blurbArray[indexPath.row]
        
        // cell background color
      
            cell.backgroundColor = UIColor.clearColor()
        
        //the color change of the cell once its clicked
        let cellBGView = UIView()
        cellBGView.backgroundColor = UIColor(red: 237.0/255.0, green: 109.0/255.0, blue: 148.0/255.0, alpha: 1)
        cell.selectedBackgroundView = cellBGView
        

        return cell
    }
 


    override func tableView(tableView: UITableView, didSelectRowAtIndexPath indexPath: NSIndexPath) {
        NSLog("You selected cell #\(indexPath.row)!")
        //unselects cell after being clicked
        self.tableView.deselectRowAtIndexPath(indexPath, animated: true)
        
        //opens URLs to news articles
        UIApplication.sharedApplication().openURL(NSURL(string: urlArray[indexPath.row])!)        
    }
    
    //


    /*
    // Override to support conditional editing of the table view.
    override func tableView(tableView: UITableView, canEditRowAtIndexPath indexPath: NSIndexPath) -> Bool {
        // Return NO if you do not want the specified item to be editable.
        return true
    }
    */

    /*
    // Override to support editing the table view.
    override func tableView(tableView: UITableView, commitEditingStyle editingStyle: UITableViewCellEditingStyle, forRowAtIndexPath indexPath: NSIndexPath) {
        if editingStyle == .Delete {
            // Delete the row from the data source
            tableView.deleteRowsAtIndexPaths([indexPath], withRowAnimation: .Fade)
        } else if editingStyle == .Insert {
            // Create a new instance of the appropriate class, insert it into the array, and add a new row to the table view
        }    
    }
    */

    /*
    // Override to support rearranging the table view.
    override func tableView(tableView: UITableView, moveRowAtIndexPath fromIndexPath: NSIndexPath, toIndexPath: NSIndexPath) {

    }
    */

    /*
    // Override to support conditional rearranging of the table view.
    override func tableView(tableView: UITableView, canMoveRowAtIndexPath indexPath: NSIndexPath) -> Bool {
        // Return NO if you do not want the item to be re-orderable.
        return true
    }
    */

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        // Get the new view controller using [segue destinationViewController].
        // Pass the selected object to the new view controller.
    }
    */
    
}
