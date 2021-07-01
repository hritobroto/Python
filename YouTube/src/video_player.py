"""A video player class."""
import random
from .video_library import VideoLibrary
from pprint import pprint
import os.path
#pVid=0
#nVid=""
class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        #self._video_playlist = Playlist()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""

        print("Here's a list of all available videos:")
        l1=self._video_library.get_all_videos()
        l=sorted(l1, key=lambda k: getattr(k,'_title')) 
        #print(l)
        for i in l:
            print(getattr(i,'_title'),end=" ")
            print(f"({getattr(i,'_video_id')})",end=" ")
            ls=getattr(i,'_tags')
            '''print("[",end="")
            for x in ls:
                print(x,end=" ")
            print("]")'''
            print ('[%s]' % ' '.join(map(str,ls)))

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """

        l=self._video_library.get_all_videos()
        
        if(self._video_library.pVid!=0):
            print(f"Stopping video: {self._video_library.nVid}")

        if(next((item for item in l if getattr(item,'_video_id') == video_id),None)):
            print("Playing video: ",end="")
            x=next(item for item in l if getattr(item,'_video_id') == video_id)
            print(getattr(x,'_title'))
            self._video_library.pVid=1
            self._video_library.nVid=getattr(x,'_title')
        else:
            print("Cannot play video: Video does not exist")


    def stop_video(self):
        """Stops the current video."""
        if(self._video_library.pVid==0):
            print("Cannot stop video: No video is currently playing")
        else:
            print(f"Stopping video: {self._video_library.nVid}")
            self._video_library.pVid=0
            self._video_library.nVid=""

    def play_random_video(self):
        """Plays a random video from the video library."""
        r=random.randint(0,4)
        l=self._video_library.get_all_videos()
        if(self._video_library.pVid!=0):
            print(f"Stopping video: {self._video_library.nVid}")
        print("Playing video: ",end="")
        x1=getattr(l[r],'_video_id')
        x=next(item for item in l if getattr(item,'_video_id') == x1)
        print(getattr(x,'_title'))
        self._video_library.pVid=1
        self._video_library.nVid=getattr(x,'_title')
        #print("play_random_video needs implementation")

    def pause_video(self):
        """Pauses the current video."""
        if(self._video_library.pVid==1):
            print(f"Pausing video: {self._video_library.nVid}")
            self._video_library.pVid=2
        #if(self._video_library.pVid==2):
        elif(self._video_library.pVid==2):
            print(f"Video already paused: {self._video_library.nVid}")
        #if(self._video_library.pVid==0):
        else:
            print("Cannot pause video: No video is currently playing")
        #print("pause_video needs implementation")

    def continue_video(self):
        """Resumes playing the current video."""
        if(self._video_library.pVid==2):
            print(f"Continuing video: {self._video_library.nVid}")
            self._video_library.pVid=1
        #if(self._video_library.pVid!=2):
        elif(self._video_library.pVid==1):
                print("Cannot continue video: Video is not paused")
        #if(self._video_library.pVid==0):
        else:
            print("Cannot continue video: No video is currently playing")
        #print("continue_video needs implementation")

    def show_playing(self):
        """Displays video currently playing."""
        l=self._video_library.get_all_videos()
        if(self._video_library.pVid==1):
            print("Currently playing: ",end="")
            x=next(item for item in l if getattr(item,'_title') == self._video_library.nVid)
            print(getattr(x,'_title'),end=" ")
            print(f"({getattr(x,'_video_id')})",end=" ")
            ls=getattr(x,'_tags')
            print ('[%s]' % ' '.join(map(str,ls)))
        elif(self._video_library.pVid==2):
            print("Currently playing: ",end="")
            x=next(item for item in l if getattr(item,'_title') == self._video_library.nVid)
            print(getattr(x,'_title'),end=" ")
            print(f"({getattr(x,'_video_id')})",end=" ")
            ls=getattr(x,'_tags')
            print ('[%s]' % ' '.join(map(str,ls)),end=" - PAUSED\n")
        else:
            print("No video is currently playing")
        #print("show_playing needs implementation")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        s=""+playlist_name+".txt"
        x=s.lower()
        #print(x)
        if(os.path.exists(x)):
            print("Cannot create playlist: A playlist with the same name already exists")
        else:
            f=open(x,'w')
            self._video_library.pLists.append(x)
            self._video_library.pListNs.append(playlist_name)
            print(f"Successfully created new playlist: {playlist_name}")


    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        l=self._video_library.get_all_videos()
        s=""+playlist_name+".txt"
        x=s.lower()
        z=0
        if(next((item for item in l if getattr(item,'_video_id') == video_id),None)):
            if(os.path.exists(x)):
                f=open(x,'a')
                ch=""+video_id+"\n"
                with open(x) as fi:
                    if ch in fi.read():
                        print(f"Cannot add video to {playlist_name}: Video already added")
                        z=1
                if(z==0):
                    f.write(ch)
                    f.close()
                    print(f"Added video to {playlist_name}:",end=" ")
                    x=next(item for item in l if getattr(item,'_video_id') == video_id)
                    print(getattr(x,'_title'))
            else:
                print(f"Cannot add video to {playlist_name}: Playlist does not exist")
        else:
            print("Cannot add video to my_cool_playlist: Video does not exist")

    def show_all_playlists(self):
        """Display all playlists."""
        pl=self._video_library.pListNs
        if(len(pl)==0):
            print("No playlists exist yet")
        else:
            print("Showing all playlists:")
            for p in pl:
                print(p)
            
        #print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        l=self._video_library.get_all_videos()
        s=""+playlist_name+".txt"
        x=s.lower()
        print(f"Showing playlist: {playlist_name}")
        if(os.stat(x).st_size==0):
            print("No videos here yet")
        else:
            with open(x) as f:
                lin = f.read()
                lin=lin[0:len(lin)-1]
                #print(lin)
                x=next(item for item in l if getattr(item,'_video_id') == lin)
                print(getattr(x,'_title'),end=" ")
                print(f"({getattr(x,'_video_id')})",end=" ")
                ls=getattr(x,'_tags')
                print ('[%s]' % ' '.join(map(str,ls)))
        
        #print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        l=self._video_library.get_all_videos()
        s=""+playlist_name+".txt"
        x=s.lower()
        z=0
        if(os.path.exists(x)):
            f=open(x,'r')
            lines = f.readlines()
            #print(lines)
            f.close()
            fi=open(x,'w')
            for line in lines:
                if(line.strip("\n")!=video_id):
                    fi.write(line)
                else:
                    z=1
            fi.close()
            if(z==1):
                print(f"Removed video from {playlist_name}:",end=" ")
                x=next(item for item in l if getattr(item,'_video_id') == video_id)
                print(getattr(x,'_title'))
            else:
                    print(f"Cannot remove video from {playlist_name}: Video does not exist")
        else:
            print(f"Cannot remove video from {playlist_name}: Playlist does not exist")
        
        #print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        l=self._video_library.get_all_videos()
        s=""+playlist_name+".txt"
        x=s.lower()
        z=0
        if(os.path.exists(x)):
            fi=open(x,'w')
            fi.write("")
            fi.close()
            print(f"Successfully removed all videos from {playlist_name}")
        else:
            print(f"Cannot clear playlist {playlist_name}: Playlist does not exist")
        #print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        s=""+playlist_name+".txt"
        x=s.lower()
        if(os.path.exists(x)):
            os.remove(x)
            print(f"Deleted playlist: {playlist_name}")
        else:
            print(f"Cannot delete playlist {playlist_name}: Playlist does not exist")
        #print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        l1=self._video_library.get_all_videos()
        l=sorted(l1, key=lambda k: getattr(k,'_title')) 
        cv=1
        d=1
        flag=0
        for cl in l:
            #print(getattr(cl,'_title'))
            if(search_term in getattr(cl,'_title').lower()):
                if(cv==1):
                    print(f"Here are the results for {search_term}:")
                    cv=3
                print(f"{d})",end=" ")
                d+=1
                print(getattr(cl,'_title'),end=" ")
                print(f"({getattr(cl,'_video_id')})",end=" ")
                ls=getattr(cl,'_tags')
                print ('[%s]' % ' '.join(map(str,ls)))
                flag=1
        if(flag==1):
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            x=input()
            lo=1
            if(x.isnumeric()):
                for cl in l:
                    #print(getattr(cl,'_title'))
                    if(search_term in getattr(cl,'_title').lower()):
                        if(lo==int(x)):
                            self.play_video(getattr(cl,'_video_id'))
                        lo+=1
        else:
            print(f"No search results for {search_term}")
        #print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        l1=self._video_library.get_all_videos()
        l=sorted(l1, key=lambda k: getattr(k,'_title')) 
        cv=1
        d=1
        flag=0
        for cl in l:
            #print(getattr(cl,'_title'))
            if(video_tag in getattr(cl,'_tags')):
                if(cv==1):
                    print(f"Here are the results for {video_tag}:")
                    cv=3
                print(f"{d})",end=" ")
                d+=1
                print(getattr(cl,'_title'),end=" ")
                print(f"({getattr(cl,'_video_id')})",end=" ")
                ls=getattr(cl,'_tags')
                print ('[%s]' % ' '.join(map(str,ls)))
                flag=1
        if(flag==1):
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            x=input()
            lo=1
            if(x.isnumeric()):
                for cl in l:
                    #print(getattr(cl,'_title'))
                    if(video_tag in getattr(cl,'_tags')):
                        if(lo==int(x)):
                            self.play_video(getattr(cl,'_video_id'))
                        lo+=1
        else:
            print(f"No search results for {video_tag}")
        #print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
