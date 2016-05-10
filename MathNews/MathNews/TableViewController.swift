//
//  TableViewController.swift
//  MathNews
//
//  Created by cs laptop on 2/16/16.
//  Copyright (c) 2016 cs121MathNewApp. All rights reserved.
//
//  This class conducts all the operations on the tableview, adding, updating, and removing cells that contain article metadata
//

import UIKit
import Firebase

class TableViewController: UITableViewController {
    //Create empty arrays for titles, blurbs, urls
    var titleArray = [String]()
    var blurbArray = [String]()
    var urlArray = [String]()

    // Pull down the article metadata into Swift
    override func viewDidAppear(animated: Bool) {
        super.viewDidAppear(animated)

        // Create reference to database at the "articles" sub-category
        let ref = Firebase(url:"https://sweltering-heat-2148.firebaseio.com/articles")

        // Retrieve new articles as they are added to your database, if no value is present for a given key, give the tableview a " "
        // instead of an empty string to avoid breaking it
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

        // Reload table with above data
        self.tableView.reloadData()

        }, withCancelBlock: { error in
                print(error.description)

        })

        // Clear all the cells when we observe Jeeves removing keys from firebase, this means an update of the articles is in progress
        ref.observeEventType(.ChildRemoved, withBlock: { snapshot in
            self.titleArray = []
            self.blurbArray = []
            self.urlArray = []
            self.tableView.reloadData()
        })

    }

    // This function runs on startup of the tableviewcontroller, it changes the color of UI elements and cleans up unoccupied cells
    override func viewDidLoad() {

        super.viewDidLoad()

        // Change the color of the navigation controller and text color
        // self.navigationController?.navigationBar.barTintColor = UIColor.lightGrayColor()
        self.navigationController?.navigationBar.titleTextAttributes = [NSForegroundColorAttributeName:UIColor(red: 0.0/255.0, green: 137.0/255.0, blue: 237.0/255.0, alpha: 1.0) ]

        //Sets the table's background to white
        self.tableView.backgroundColor = UIColor.whiteColor()

        //Gets rid of the unoccupied cells
        tableView.tableFooterView = UIView(frame:CGRectZero)
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    override func numberOfSectionsInTableView(tableView: UITableView) -> Int {
        // Return the number of sections.
        return 1
    }

    override func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        // Return the number of rows in the section.
        return titleArray.count
    }

    // This function displays the correct data inside the cell, and it changes the cell's color once it is clicked.
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

        //Change color of the cell once its clicked
        let cellBGView = UIView()
        cellBGView.backgroundColor = UIColor(red: 237.0/255.0, green: 109.0/255.0, blue: 148.0/255.0, alpha: 1)
        cell.selectedBackgroundView = cellBGView

        return cell
    }

    // This function registers a user's selection of the cell, and navigates to the specified URL
    override func tableView(tableView: UITableView, didSelectRowAtIndexPath indexPath: NSIndexPath) {
        NSLog("You selected cell #\(indexPath.row)!")
        //Unselects cell after being clicked
        self.tableView.deselectRowAtIndexPath(indexPath, animated: true)

        //Opens URLs to news articles in Safari
        UIApplication.sharedApplication().openURL(NSURL(string: urlArray[indexPath.row])!)
    }
}
