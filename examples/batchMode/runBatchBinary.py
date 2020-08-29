#!/usr/bin/env python3
import datetime
import logging
import os
import sys
 
import batchRunner
 
class binaryFrameProcessor(batchRunner.frameProcessor):
    '''defines details for using a binary executable in a simple batch job'''
 
    def installerCmd( self ):
        return None

    workerScriptPath = 'helloFrame_aarch64'  # binary to copy to instance
 
    def frameOutFileName( self, frameNum ):
        return 'frame_%d.out' % (frameNum)

    def frameCmd( self, frameNum ):
        workerScriptFileName = os.path.basename( self.workerScriptPath )
        cmd = './%s %d > %s' % \
            (workerScriptFileName, frameNum, self.frameOutFileName(frameNum))
        return cmd
 
if __name__ == "__main__":
    # configure logger
    logging.basicConfig()
    dateTimeTag = datetime.datetime.now().strftime( '%Y-%m-%d_%H%M%S' )
    outDataDirName = 'data/binary_' + dateTimeTag

    rc = batchRunner.runBatch(
        frameProcessor = binaryFrameProcessor(),
        commonInFilePath = binaryFrameProcessor.workerScriptPath,
        filter = '{"cpu-arch": "aarch64", "dpr": ">=24"}',
        authToken = 'YourAuthTokenHere',
        timeLimit = 1200,
        instTimeLimit = 120,
        frameTimeLimit = 120,
        outDataDir = outDataDirName,
        encryptFiles = False,
        startFrame = 1,
        endFrame = 3
    )
    sys.exit( rc )